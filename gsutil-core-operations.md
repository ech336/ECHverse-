---
name: gsutil-core-operations
description: Core operations for Google Cloud Storage management using gsutil. Use for copy, sync, list, remove, and bucket creation tasks.
---

# gsutil Core Operations

This skill provides a core set of commands for interacting with Google Cloud Storage via `gsutil`.

## Core Commands Reference

| Operation | Command Syntax | Description |
| :--- | :--- | :--- |
| **Copy Objects** | `gsutil cp [FILE_PATH] gs://[BUCKET_NAME]` | Uploads or copies files to a storage bucket. |
| **Sync Directories** | `gsutil -m rsync -r [LOCAL_DIR] gs://[BUCKET_NAME]` | Synchronizes local content with a bucket recursively. |
| **List Buckets** | `gsutil ls` | Displays all accessible storage buckets. |
| **Remove Objects** | `gsutil rm gs://[BUCKET_NAME]/[OBJECT_NAME]` | Deletes a specified object from a bucket. |
| **Create Buckets** | `gsutil mb gs://[BUCKET_NAME]` | Provisions a new Google Cloud Storage bucket. |

## Execution Parameters

### Parallel Processing (`-m` flag)
Speeds up large-scale multi-file operations (such as `cp`, `rm`, and `rsync`) by executing commands in parallel across multiple threads/processes.

**Example: High-speed parallel directory sync**
`gsutil -m rsync -r [LOCAL_DIR] gs://[BUCKET_NAME]`
