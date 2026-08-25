# GitHub Publishing Guide

This guide publishes the complete repository and then attaches the installable skill ZIP as a release asset.

## Repository details

- **Repository name:** `rigorous-ai-research-coding`
- **Description:** `A manually invoked, evidence-first ChatGPT/Codex skill for trustworthy Python research engineering across ML/DL, generative AI, time series, and reinforcement learning.`
- **Visibility:** Public
- **Initial version:** `0.1.0-beta`
- **Release tag:** `v0.1.0-beta`
- **License:** MIT

## Part 1 — Upload the repository

1. Download `Rigorous_AI_Research_Coding_GitHub_Repository_v0.1.0-beta.zip`.
2. Extract this repository ZIP on your computer.
3. On GitHub, select the **+** menu and choose **New repository**.
4. Enter the repository name and description above.
5. Choose **Public**.
6. Do **not** add a README, `.gitignore`, or license on the creation screen because the package already contains them. GitHub warns that pre-populating an imported repository can create merge conflicts.
7. Select **Create repository**.
8. In the empty repository, choose **uploading an existing file** or **Add file → Upload files**.
9. Open the extracted folder and drag its **contents** into GitHub. Do not upload the repository ZIP as the repository content. The root should show `README.md`, `LICENSE`, `CITATION.cff`, `skill/`, `docs/`, `evals/`, and `tests/`.
10. Enter `Initial beta release` as the commit message and choose **Commit changes**.

GitHub's browser uploader currently accepts up to 100 files at once and limits browser-uploaded individual files to 25 MiB. This package is within those limits. Official instructions: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

If dragging folders does not preserve the structure, use GitHub Desktop or the command-line method described in the same official documentation. Do not flatten the folders.

## Part 2 — Confirm repository structure

Check that this exact path opens:

```text
skill/rigorous-ai-research-coding/SKILL.md
```

Also check:

```text
skill/rigorous-ai-research-coding/agents/openai.yaml
.github/workflows/validate.yml
```

Open the **Actions** tab and verify that **Validate skill** passes. If GitHub asks to enable Actions, enable workflows for this repository.

## Part 3 — Create the beta release

1. Download `Rigorous_AI_Research_Coding_Skill_v0.1.0-beta.zip` but **do not extract it**. This is the installable release asset.
2. Open the repository on GitHub.
3. Select **Releases** and then **Draft a new release**.
4. Select **Choose a tag**, type `v0.1.0-beta`, and create the tag from `main`.
5. Set the release title to `Rigorous AI Research Coding v0.1.0-beta`.
6. Use these release notes:

```text
First public beta of Rigorous AI Research Coding.

- Manual-only activation for shared-account safety
- Evidence-first Python research engineering workflow
- ML/DL, generative-AI, time-series, and RL guidance
- Split, configuration, provenance, hashing, and result-bundle validators
- Behavioral evaluation suite and scientific evidence report

Status: structurally and deterministically tested beta. Independent forward-agent validation remains future work.
```

7. Drag `Rigorous_AI_Research_Coding_Skill_v0.1.0-beta.zip` into the release attachment area.
8. Wait until the filename and upload size appear.
9. Select **Set as a pre-release**. A prerelease cannot be set as the repository's latest full release, so the “Set as latest release” option may be absent or disabled.
10. Select **Publish release**.

GitHub recommends drafting a release and attaching all assets before publishing, especially when immutable releases are enabled: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository

## Part 4 — Verify the public release

1. Open the published release page.
2. Under **Assets**, click `Rigorous_AI_Research_Coding_Skill_v0.1.0-beta.zip`.
3. Confirm that the download begins.
4. Compare the downloaded SHA-256 value with `RELEASE_ASSET_SHA256.txt` in the repository.
5. Open the ZIP locally and verify that it contains one top-level folder named `rigorous-ai-research-coding`.

## Part 5 — Install and invoke

Upload the installable skill ZIP to the ChatGPT/Codex skills area without extracting it when ZIP upload is supported. Then test in a fresh chat:

```text
Use $rigorous-ai-research-coding to state your coding boundary and list the evidence labels you will use. Do not modify files.
```

Then send a normal coding request without naming the skill. It should not activate automatically.

## When to publish 1.0.0

Keep the beta label until the behavioral cases in `evals/behavior_cases.md` pass across repeated fresh sessions and at least two representative real repositories, with all failures preserved. Do not promote based only on structural validation or one successful chat.

## Official GitHub references

- Create a repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- Add files: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Manage releases: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- CITATION files: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
