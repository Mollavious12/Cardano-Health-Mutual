# CareChain Web Platform Development Plan

## Current Goal
Build a complete web platform for mutual healthcare access with community-driven financing, health education, and digital inclusivity.

---

## Phase 1: Landing Page & Core Layout ✅
- [x] Create hero section with mission statement "Affordable. Inclusive. Smart Healthcare Access"
- [x] Build "How It Works" section explaining mutual contributions → health coverage → transparency
- [x] Add community impact statistics dashboard (members, funds raised, lives supported)
- [x] Implement navigation bar with links to Dashboard, Learning Hub, About, Contact
- [x] Add prominent CTA buttons: "Join a Mutual" and "Learn Health Finance"
- [x] Create footer with links and social media
- [x] Apply modern design with purple/gray theme matching CareChain branding

---

## Phase 2: User Authentication & Dashboard Foundation ✅
- [x] Implement Clerk authentication (signup, login, logout) - REPLACED Supabase with Clerk
- [x] Integrate reflex-clerk-api with app wrapping and user state registration
- [x] Add Clerk sign-in and sign-up pages (/sign-in and /sign-up)
- [x] Update navbar with Clerk sign-in/sign-up buttons and user_button
- [x] Create role-based access control using ClerkUser state
- [x] Build main dashboard layout with sidebar navigation
- [x] Create "My Wallet" page showing contribution balance and transaction history
- [x] Build "Health Coverage" page listing available mutual health plans
- [x] Add "Claims" page for submitting and tracking claim status
- [x] Implement user profile management with Clerk user_profile component
- [x] Update sidebar to display ClerkUser data (first_name, email_address)
- [x] Create responsive dashboard design for mobile and desktop

---

## Phase 3: Health Education Hub & Financial Mutual Engine
- [ ] Build Learning Hub with categories: Preventive Health, Nutrition, Mental Health, Financial Literacy
- [ ] Create course cards with progress tracking and completion badges
- [ ] Implement article/video content display with multimedia support
- [ ] Add certificate generation for completed courses
- [ ] Build Financial Mutual Engine with smart pooling dashboard
- [ ] Create contribution interface with mobile money integration (MTN, Airtel, M-Pesa simulation)
- [ ] Implement real-time fund transparency dashboard showing inflow, outflow, and claims
- [ ] Add claim submission and verification workflow
- [ ] Create Community Chat interface for peer discussions
- [ ] Build Admin Panel for managing users, providers, claims, and fund analytics
- [ ] Add visual analytics with charts for fund health monitoring

---

## Notes
- **Authentication**: Using Clerk (reflex-clerk-api) for authentication with environment variables:
  - CLERK_PUBLISHABLE_KEY
  - CLERK_SECRET_KEY
- MongoDB available for additional data storage if needed
- Focus on mobile-first responsive design
- Purple/gray color scheme matching CareChain branding
- Prioritize accessibility and clarity for low-literacy users
- **Important**: Clerk authentication does NOT work in iframes (security policy) - test in new tab when deployed