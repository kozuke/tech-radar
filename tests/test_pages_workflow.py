from pathlib import Path


PAGES_WORKFLOW = Path(".github/workflows/pages.yml")
PREPARE_SITE_SCRIPT = Path("scripts/prepare-site-data.mjs")


def test_slack_button_links_to_daily_digest_page():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert 'DIGEST_PAGE_PATH: ${{ needs.build.outputs.digest_page_path }}' in workflow
    assert 'TARGET_PAGE_URL="${PAGE_URL%/}/$DIGEST_PAGE_PATH"' in workflow
    assert '--arg page_url "$TARGET_PAGE_URL"' in workflow
    assert "url: $page_url" in workflow


def test_deploy_job_does_not_checkout_repository_before_using_slack_secret():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")
    deploy_section = workflow.split("  deploy:", maxsplit=1)[1]
    notify_section = deploy_section.split("      - name: Notify Slack", maxsplit=1)[0]

    assert "actions/checkout" not in notify_section


def test_workflow_run_deploys_only_when_data_or_site_changed():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert "  detect_changes:" in workflow
    assert 'git diff --name-only "$WORKFLOW_RUN_HEAD_SHA"..HEAD -- data site' in workflow
    assert "needs.detect_changes.outputs.should_deploy == 'true'" in workflow


def test_pages_workflow_uses_root_build_script_to_prepare_site_data():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert "working-directory: site" not in workflow
    assert "run: npm run build" in workflow


def test_prepare_site_script_copies_digest_pages_for_vitepress():
    script = PREPARE_SITE_SCRIPT.read_text(encoding="utf-8")

    assert "siteArticlesDir" in script
    assert "'site', 'public', 'data'" in script
    assert "endsWith('__daily-digest.md')" in script
    assert "hideSlackSummarySection" in script
    assert 'slack-summary-only" hidden aria-hidden="true"' in script
    assert "const sanitized = hideSlackSummarySection(raw)" in script
