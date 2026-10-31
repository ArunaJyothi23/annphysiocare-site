# Ann Physiocare – new website (static)

## Hosting
Upload the **contents of this folder** (not `_src/`) to the web root of the domain. Paths are root-absolute (`/assets/...`), so it must live at the domain root, not a sub-folder. Works on Apache (`.htaccess`), Netlify/Cloudflare Pages (`_redirects`, `404.html`) or any static host (nginx: `try_files $uri $uri/ =404;`). Local preview: `python3 -m http.server` in this folder.

## Before launch (needs you)
1. **Logo** → `assets/img/logo.png` (and `assets/img/annpetspolicy.png`).
2. **AI images/video** → see `AI-PROMPTS.md` (filenames + prompts). Pages look complete without them (gradient + icon slots).
3. **Policy PDFs** → copy the 4 PDFs into `upload/` (names in AI-PROMPTS.md).
4. **Forms** (contact, careers, referral): set `FORM_ENDPOINT` at the top of `assets/js/main.js` (Formspree/Getform/your handler). Until set, forms open the visitor's email app addressed to rehab@annphysiocare.com (careers: hr@annphysiocare.com). File uploads (CV, referral attachments) need a real endpoint.
5. **Staff login** is a placeholder; the original used a password gate – implement real authentication server-side.
6. The original's **live-chat widget** is not included.
7. Cookie banner: Google Analytics (G-EWQB7CDNMZ) loads only after "Statistics" consent.

## Source discrepancies to confirm
- Clinic count appears as 60+ (home/services) and 85+ (about); both kept verbatim.
- Shockwave pricing: £80/£60 on the detail page, £85/£65 on Pricing; both kept.
- The "3 sessions for £110" button on the original FAQ linked to the £45 Stripe link; here FAQ keeps that, Pricing uses the dedicated link.
- Some careers posts list a different location in the title vs. body (kept as published).
- Original content typos retained to preserve wording; edit freely.

## Rebuild
Source generators live in `_src/` (`python3 _src/build.py` regenerates all pages). Edit CSS in `assets/css/style.css`, scripts in `assets/js/main.js`.

## SEO meta
Titles, descriptions and keywords of the 84 clinic pages, the RCS In-Work Support page, and the Terms/Privacy titles are copied from the live site (`_src/meta.tsv`). Other pages' original descriptions/keywords were blank, so the descriptions written here are kept. All pages have `robots: index, follow` (staff-login is noindex). Canonicals point to each page's own clean URL (the original canonicals on a few clinics pointed at the wrong clinic, e.g. Chippenham → Crawley, Walton-on-Thames → Weybridge, East Ham → Forest Gate).
