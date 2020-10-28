# Integration testing Wellcome Collection

Runs some integration tests to ensure that our staging environments are passing tests and it's safe to perform a deployment to production.

This pipeline runs in [Buildkite](https://buildkite.com/wellcomecollection/integration) and is triggered when [catalogue](https://buildkite.com/wellcomecollection/catalogue) or [wellcomecollection.org](https://buildkite.com/wellcomecollection/wellcomecollection.org) are deployed to staging.

[![Build status](https://badge.buildkite.com/31a06ac64ab4f09ca5bc5930e21a57889c3f02561260f18ae6.svg?branch=main)](https://buildkite.com/wellcomecollection/integration)
