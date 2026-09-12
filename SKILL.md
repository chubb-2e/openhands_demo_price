---
name: safe-bugfix
description: Use this skill when fixing a reported software bug safely and systematically.
triggers:
  - bug fix
  - fix bug
  - reported bug
  - safe bugfix
---

# Safe Bugfix

Use this workflow whenever you are asked to fix a reported bug.

## Procedure

1. Read the issue or bug report first.
2. Run the existing tests before changing any code.
3. Reproduce the reported bug yourself.
4. Identify the root cause.
5. Add a regression test that fails because of the bug.
6. Fix only the code necessary to solve the issue.
7. Run the relevant tests again and confirm that they pass.
8. Delegate the final code review to a sub-agent.
9. Incorporate valid reviewer feedback if needed.
10. Summarize:
   - root cause
   - files changed
   - tests performed
   - reviewer feedback
   - remaining risks
