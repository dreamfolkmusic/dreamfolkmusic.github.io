# Dreamfolk — approved vintage robot design

The static site remains in the repository root, published by GitHub Pages at dreamfolkmusic.com.

## Artwork and design

- Source: the user's approved 1199 × 1312 vintage robot website mockup, supplied on November 26, 2026. No replacement or generated robot art is used.
- The original square teal robot, round golden robot, golden moon, poppies, sleeve/vinyl, guitar, tape reel and flower illustrations are reused through CSS image windows. The original wordmark is image artwork with an accessible name. Content, links and navigation are live HTML rather than screenshot hotspots.
- `assets/vintage-mockup.jpg` is a 1199 × 1312 optimized JPEG; `assets/vintage-mockup-small.jpg` is an 800 × 875 mobile variant. Multiple image windows share the same cached source. The original 3.2 MB PNG is not loaded by visitors. JPEG files are approximately 763 KB and 276 KB respectively.
- A distressed border reuses the mockup's edge; parchment and teal surfaces use a lightweight SVG grain texture. IM Fell English and Oswald are hosted locally with their SIL Open Font Licenses.
- Desktop follows the approved robot/wordmark hero, release/band row and three illustrated navigation panels. Mobile stacks the hero and content, with smaller dedicated illustration windows in horizontal navigation cards.

## Preserved content and deliberate deviations

- The actual release remains **debut single coming soon**, with **no release date announced**. “Perfect Strangers,” “New single,” Spotify and Apple Music in the illustrative mockup are not treated as confirmed release information or active accounts.
- The sleeve is decorative visual branding, not a newly announced release cover. The primary button says “Explore the music” and leads to the existing SoundCloud and YouTube channels; no unsupported playable single is implied.
- All existing external music/social URLs, professional email, original-songwriting/AI-production identity, fictional duo background and member descriptions are retained. The existing story and contact/social content continues beneath the mockup's three panels.
- Existing SEO title, descriptions, canonical URL, Open Graph/Twitter metadata, artist JSON-LD, sitemap, robots, favicon and CNAME are preserved. The theme color is updated to teal. The existing studio social-preview image is intentionally retained, rather than exposing the flattened mockup's unconfirmed release title in link previews.
- The Cloudflare Web Analytics script and token are preserved exactly once, immediately before `</body>`.
- No mailing list, third-party form, new streaming account, release title, audio or date is invented.

## Source limitation

The supplied approved mockup is a flattened image. Original layered files, separate transparent illustrations and a higher-resolution version were not available. CSS windows preserve the original characters and illustrations without redrawing them. The surrounding textures, body typography, button sizing and responsive reflow are recreations rather than pixel-identical layered exports. Archived artwork remains in the repository and is not substituted for the approved robots.

## Validation

Run `python3 scripts/verify-site.py` to check structure, local resources, anchors, original links, analytics, release claims and preserved SEO against the pre-redesign commit. Browser-reviewed at 320, 390, 768, 1200 and 1440 CSS pixels. No horizontal overflow or off-screen text/link boxes at the checked widths. Mobile artwork selection, desktop artwork loading, main navigation, illustrated contact link and keyboard skip-to-content were checked. Skip-to-content moved focus to the main landmark. This is a focused accessibility review, not a complete assistive-technology audit. Email delivery, third-party account behavior and external social-preview cache refresh are not asserted. Deployment verification is reported in the task handoff.
