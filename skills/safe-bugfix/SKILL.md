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

## Core Procedure

1. Read the issue or bug report first.
2. Run the existing tests before changing any code.
3. Reproduce the reported bug yourself.
4. Identify the root cause.
5. Add a regression test that fails because of the bug.
6. Fix only the code necessary to solve the issue.
7. Run the relevant tests again and confirm that they pass.
8. Delegate the final code review to a reviewer sub-agent.
9. Incorporate valid reviewer feedback if needed.
10. Summarize the final result.

---

# Demo Output Rules

The visible output is for a live demo.

The main workflow stages must be visually obvious at a glance.

Use the exact stage banners below whenever the workflow reaches that stage.

## Stage Banners

### 🧭 QUEST
Briefly restate the task in one or two lines.

Example:

🧭 QUEST  
Fix the bug reported in `ISSUE.md` using the safe-bugfix workflow.

---

### 🧪 STEP 1 — EXISTING TESTS
Before changing any code, announce that the existing tests are being checked.

After the test run, use one of these:

✅ EXISTING TESTS PASSED  
or  
❌ EXISTING TESTS FAILED

Keep the explanation short.

---

### 🐞 STEP 2 — BUG REPRODUCTION
Announce that the reported bug is being reproduced.

If reproduced, show:

⚠️ BUG REPRODUCED  
<one short sentence describing the incorrect result>

Example:

⚠️ BUG REPRODUCED  
`calculate_final_price(10000, 20)` returned `9980` instead of `8000`.

---

### 🔍 STEP 3 — ROOT CAUSE
State the root cause in one short sentence.

Example:

🔍 ROOT CAUSE  
The discount percentage was treated as a fixed amount instead of a percentage of the price.

---

### 🛠 STEP 4 — REGRESSION TEST + FIX
Announce that a regression test is being added and the minimal code fix is being applied.

Show the important changed code when useful.

Keep the explanation concise.

---

### ✅ STEP 5 — VERIFICATION
Run the relevant tests after the fix.

Then show:

✅ ALL TESTS PASSED

Include the number of tests when available.

Example:

✅ ALL TESTS PASSED  
`4 passed`

---

### 🤝 STEP 6 — DELEGATION
Before creating or invoking the reviewer sub-agent, clearly show:

🤝 DELEGATION  
Sending the completed fix to a reviewer agent for independent code review.

Then delegate the review.

Do not hide the delegation step inside a long paragraph.

---

### 👀 REVIEWER RESULT
When the reviewer agent finishes, show the reviewer result clearly.

Example:

👀 REVIEWER RESULT  
Approve — no blocking issues.

Then list only the most important reviewer feedback.

If reviewer feedback is incorporated, show:

🔁 REVIEW FEEDBACK APPLIED  
<short description of what was changed>

---

### ✅ FINAL RESULT
End with a compact final summary.

Use this structure:

✅ FINAL RESULT

- Root cause:
- Files changed:
- Tests:
- Reviewer result:
- Remaining risks:

Keep this section concise and presentation-friendly.

---

# Noise Reduction Rules

The visible output should emphasize the quest stages, not internal troubleshooting.

Follow these rules:

1. Do not announce every small syntax correction, typo fix, command retry, formatting correction, or temporary-file cleanup as a major step.
2. If you make a small internal mistake while executing a command or editing code, correct it quietly and continue.
3. Do not create a new stage banner for minor self-corrections.
4. Do not write long explanations about temporary command failures unless they prevent progress.
5. Tool retries, temporary verification scripts, encoding fixes, shell quoting fixes, and cleanup operations should remain visually secondary.
6. Keep intermediate commentary short.
7. The audience should be able to identify the main workflow by scanning only the emoji stage banners.
8. Always announce the workflow stage first, then perform the action.
9. Do not expose private credentials, API keys, encrypted secrets, or other sensitive configuration details in visible summaries.
10. The final visible story should remain:

🧭 QUEST  
→ 🧪 EXISTING TESTS  
→ 🐞 BUG REPRODUCTION  
→ 🔍 ROOT CAUSE  
→ 🛠 FIX  
→ ✅ VERIFICATION  
→ 🤝 DELEGATION  
→ 👀 REVIEWER RESULT  
→ ✅ FINAL RESULT

---

# Final Review Requirements

The reviewer sub-agent should check:

- whether the fix correctly resolves the reported bug
- whether unrelated code was changed
- whether the regression test is meaningful
- whether important edge cases remain
- whether there are any blocking issues

The reviewer should return a concise verdict such as:

- Approve
- Approve with non-blocking suggestions
- Changes requested

The main agent should incorporate valid feedback when appropriate, rerun the tests, and then produce the final result.
