# Git SSH Setup Guide

This guide covers setting up Git with SSH authentication for secure connections to GitHub.

## Step 1: Configure Git User Information

Set your global Git username and email:

```bash
git config --global user.name "[insert username]"
git config --global user.email "[insert anonymous github email provided]"
```

### Verify Configuration

Verify that your settings were applied correctly:

```bash
git config --get user.name
git config --get user.email
```

## Step 2: Generate SSH Key

Create a new SSH key using the ED25519 algorithm:

```bash
ssh-keygen -t ed25519 -C "[insert anonymous github email provided]"
```

When prompted, press **Enter** three times to accept the default settings (no passphrase).

### Key Location

Your SSH key pair will be generated in the `~/.ssh/` directory:

- **Private key**: `~/.ssh/id_ed25519` (keep this secret)
- **Public key**: `~/.ssh/id_ed25519.pub` (add this to GitHub)

## Step 3: Add SSH Key to GitHub

1. Copy your public key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

2. Go to GitHub Settings → SSH and GPG keys
3. Click "New SSH key" and paste your public key

## Ready to Go!

Your Git and SSH setup is now complete. You can now securely clone, push, and pull from GitHub repositories.
