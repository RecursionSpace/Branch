# Update Management

Branch provides a framework for updating software on a device. The update process can be initiated programmatically or manually called by the user.

## Workflow

To ensure a successful update Branch enforces the following workflow:

1. Check if the update is available
2. Retrieve the update
3. Verify file integrity
4. Create a backup of the current version
5. Pre-update tasks
6. Update
7. Post-update tasks
8. Restart the service
9. Verify success

## Public Repository

The easiest update to setup is via a public repository.
