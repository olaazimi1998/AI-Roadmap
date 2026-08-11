Broadcasting Rules
────────────────────────────

1. Compare shapes from RIGHT → LEFT

2. Dimensions are compatible when:
   - They are equal
   - OR one dimension is 1
   - OR one array has no dimension (scalar)

Examples:

(2, 3) + (3,)      ✅

(3, 1) + (3, 4)    ✅

(2, 3) + (2, 4)    ❌

(4, 3) + 10        ✅