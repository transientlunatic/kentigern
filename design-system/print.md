# Print

Print follows the same rules as the screen, with a smaller palette and no tints that cannot be reproduced.

## Business card

85 × 55 mm, double-sided; see the Business card preview. Front is solid `primary` with fine ripple lines, the DW ligature and the name. Back is Parchment with the name, affiliation, address, email, a QR code to the site and the Glasgow footer.

## Colour for print

Use two colours. Approximate CMYK for proofing (naive conversions; proof against a swatch before printing, because print will not match the screen):

| Token | Hex | Approx. CMYK |
|---|---|---|
| `primary` (light) | #2D6A7F | 65 / 16 / 0 / 50 |
| `ink` (light) | #2C1E10 | 0 / 33 / 64 / 83 |
| `surface` (light) | #F4F2F0 | 0 / 1 / 2 / 4 |

Uncoated cream or white stock looks right with these; a gloss coating does not. Spot inks are better than CMYK for the teal; ask the printer for the nearest match to #2D6A7F.

## Rules

- 3 mm bleed, 5 mm safe margin, fonts outlined, no type below 6pt, no line below 0.25pt.
- Line art (ripples, rules) stays at least 70% tint so it holds on the press.
- Add alt-text-equivalent: put the address in text as well as in the QR code.
