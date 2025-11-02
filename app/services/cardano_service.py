import os
import logging
from typing import Optional
import pycardano as pc
from blockfrost import BlockFrostApi, ApiError


class CardanoService:
    """Service for interacting with the Cardano blockchain."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.network = pc.Network.TESTNET
        self.api_key = os.environ.get("BLOCKFROST_API_KEY", "")
        self.api = None
        if self.api_key:
            try:
                self.api = BlockFrostApi(
                    project_id=self.api_key,
                    base_url=pc.BlockFrostChainContext.API_URL_PREPROD,
                )
                self.context = pc.BlockFrostChainContext(
                    self.api_key, base_url=pc.BlockFrostChainContext.API_URL_PREPROD
                )
                self.logger.info("CardanoService initialized with BlockFrost API.")
            except Exception as e:
                self.logger.exception(f"Failed to initialize BlockFrost API: {e}")
        else:
            self.logger.warning(
                "BLOCKFROST_API_KEY not set. CardanoService is in offline mode."
            )

    def is_online(self) -> bool:
        """Check if the service is connected to BlockFrost."""
        return self.api is not None

    def generate_wallet(self) -> Optional[dict]:
        """Generate a new Cardano wallet (payment and stake keys)."""
        try:
            payment_signing_key = pc.PaymentSigningKey.generate()
            payment_verification_key = pc.PaymentVerificationKey.from_signing_key(
                payment_signing_key
            )
            stake_signing_key = pc.StakeSigningKey.generate()
            stake_verification_key = pc.StakeVerificationKey.from_signing_key(
                stake_signing_key
            )
            address = pc.Address(
                payment_part=payment_verification_key.hash(),
                staking_part=stake_verification_key.hash(),
                network=self.network,
            )
            return {
                "address": str(address),
                "payment_skey": payment_signing_key.to_json(),
                "payment_vkey": payment_verification_key.to_json(),
                "stake_skey": stake_signing_key.to_json(),
                "stake_vkey": stake_verification_key.to_json(),
            }
        except Exception as e:
            self.logger.exception(f"Error generating wallet: {e}")
            return None

    async def get_address_info(self, address: str) -> Optional[dict]:
        """Get information about a specific address from BlockFrost."""
        if not self.is_online():
            self.logger.warning("Cannot get address info: offline mode.")
            return None
        try:
            address_info = self.api.address(address)
            utxos = self.api.address_utxos(address)
            balance = sum((int(utxo.amount[0].quantity) for utxo in utxos))
            return {
                "address": address_info.address,
                "balance_lovelace": balance,
                "utxo_count": len(utxos),
            }
        except ApiError as e:
            self.logger.exception(f"BlockFrost API error getting address info: {e}")
            return None

    def create_pool_multisig_script(self, verifier_vkeys: list[str]) -> Optional[str]:
        """Create a 2-of-3 multi-signature native script for the pool."""
        if len(verifier_vkeys) != 3:
            self.logger.error("Multi-sig script requires exactly 3 verifier keys.")
            return None
        try:
            scripts = []
            for vkey_json in verifier_vkeys:
                vkey = pc.PaymentVerificationKey.from_json(vkey_json)
                scripts.append(pc.ScriptPubkey(vkey.hash()))
            multisig_script = pc.ScriptAll(
                [pc.ScriptAny(scripts), pc.ScriptNofK(2, scripts)]
            )
            return multisig_script.to_json()
        except Exception as e:
            self.logger.exception(f"Error creating multi-sig script: {e}")
            return None

    async def build_contribution_tx(
        self, from_address: str, pool_address: str, amount_lovelace: int
    ) -> Optional[str]:
        """Build a transaction for a member's contribution."""
        if not self.is_online():
            self.logger.warning("Cannot build transaction: offline mode.")
            return None
        try:
            builder = pc.TransactionBuilder(self.context)
            builder.add_input_address(from_address)
            builder.add_output(
                pc.TransactionOutput.from_primitive([pool_address, amount_lovelace])
            )
            return builder.build().to_cbor_hex()
        except Exception as e:
            self.logger.exception(f"Error building contribution transaction: {e}")
            return None