# Dependencies

## Event ownership

| Surface | Owns economic event? | Role |
|---|---:|---|
| Purchase entry | Yes | Creates project/material cost |
| Supplier payment | No | Settles payable and cash state |
| Project report | No | Derives presentation from accepted events |

## Frozen integration example

`ProjectLink-01` maps operational allocation labels to canonical projects. It is independently verified and remains frozen during nearby module reconstruction.

## Reconstruction order

If the central Project module becomes unreliable, audit independent purchase/payment/report/settings boundaries first, then rebuild the Project core from those accepted dependency contracts.
