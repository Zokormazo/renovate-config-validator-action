#!/usr/bin/env python3
"""
MintMaker Global Config Generator

This script creates a temporary global config.js file that mimics MintMaker's behavior.

MintMaker injects repositories configuration at the GLOBAL level, not into individual repository configs.
This script creates a temporary config.js file with the same injection logic as MintMaker.

This follows the proper Renovate architecture:
- Global config (config.js): Contains repositories array with baseBranchPatterns
- Repository config (renovate.json): Contains packageRules and other repo-specific settings

References to MintMaker's injection logic:
- baseBranches injection: https://github.com/konflux-ci/mintmaker/blob/main/internal/component/github/github.go#L407-L411
- DependencyUpdateCheck controller: https://github.com/konflux-ci/mintmaker/blob/main/internal/controller/dependencyupdatecheck_controller.go#L485

This replicates MintMaker's behavior without polluting the user's repository configuration.
"""

import json
import os


def main():
    repository = os.environ.get('REPOSITORY', 'konflux-ci/fake-repo')
    base_branches_str = os.environ.get('BASE_BRANCHES', 'main')
    base_branches = [b.strip() for b in base_branches_str.split(',') if b.strip()]
    
    print(f"🏗️  Creating MintMaker global config")
    print(f"🏪 Repository: {repository}")
    print(f"🌿 Base branches: {base_branches}")
    
    # Create MintMaker's global configuration
    # This is what MintMaker injects at the global level (lines 407-411 in github.go)
    global_config = {
        "platform": "github",
        "endpoint": "https://api.github.com/",
        "gitAuthor": "mintmaker[bot] <mintmaker[bot]@users.noreply.github.com>",
        "username": "mintmaker[bot]",
        "repositories": [
            {
                "repository": repository,
                "baseBranchPatterns": base_branches
            }
        ]
    }
    
    # Write as JavaScript module (config.js format)
    config_js_content = f"module.exports = {json.dumps(global_config, indent=2)};\n"
    
    with open('config.js', 'w') as f:
        f.write(config_js_content)
    
    print("✅ Created temporary config.js with MintMaker's global configuration")
    print(f"🏪 Injected repository: {repository} with baseBranchPatterns: {base_branches}")
    print("📁 Repository config will be validated with proper global context")
    
    return 'config.js'


if __name__ == "__main__":
    main()
