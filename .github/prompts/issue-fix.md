# OpenHands Issue Resolution Workflow

Use the `safe-bugfix` skill available in this repository.

Follow the repository's safe-bugfix workflow.

Your task is to resolve the GitHub issue provided above.

## Required workflow

1. Read and understand the GitHub issue.
2. Inspect the relevant source code and existing tests.
3. Run the existing tests before changing the code.
4. Reproduce the reported bug.
5. Identify the root cause.
6. Add meaningful regression tests for the reported bug.
7. Apply the smallest necessary code fix.
8. Run the full relevant test suite and verify the fix.
9. Delegate the final code review to an independent reviewer sub-agent.
10. Review the reviewer agent's feedback.
11. If valid feedback is provided:
    - apply the feedback,
    - rerun the tests,
    - verify that all tests still pass.
12. Summarize:
    - root cause,
    - code changes,
    - tests added or modified,
    - final test result,
    - reviewer verdict,
    - reviewer feedback applied,
    - remaining risks.

## GitHub delivery

When the work is complete:

- keep the changes scoped only to this issue,
- commit the completed changes,
- create a new branch if necessary,
- create a pull request that references the GitHub issue,
- provide a concise final report.
