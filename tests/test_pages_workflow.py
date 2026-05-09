from pathlib import Path


PAGES_WORKFLOW = Path(".github/workflows/pages.yml")


def test_slack_button_links_to_daily_digest_page():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert 'TARGET_PAGE_URL="${PAGE_URL%/}/articles/${DIGEST_DATE}__daily-digest.html"' in workflow
    assert '--arg page_url "$TARGET_PAGE_URL"' in workflow
    assert "url: $page_url" in workflow


def test_deploy_job_does_not_checkout_repository_before_using_slack_secret():
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")
    deploy_section = workflow.split("  deploy:", maxsplit=1)[1]
    notify_section = deploy_section.split("      - name: Notify Slack", maxsplit=1)[0]

    assert "actions/checkout" not in notify_section
