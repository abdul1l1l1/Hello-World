---
name: GitHub repository saves
description: How to save project snapshots when the terminal Git remote rejects its stored credentials.
---

Use the attached GitHub connection API to create blobs, a tree, a commit, and update the branch reference when terminal pushes fail authentication.

**Why:** Attaching the GitHub connection does not replace stale credentials used by the terminal Git client, so retrying the same push still fails.

**How to apply:** Attempt the normal push first. If GitHub rejects the stored username or token, use the authenticated connector API to upload the tracked snapshot and verify the resulting commit.