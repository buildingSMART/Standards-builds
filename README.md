# Standards builds

This repository contains mainly auto-generated and published artefacts for the openBIM standards, including Industry Foundation Classes (IFC) specifications and Information Delivery Specification (IDS).

The contents are derived from buildingSMART specification sources and are intended to provide machine-readable outputs such as HTML pages, EXPRESS schemas, XML/XSD schemas, property set definitions, and related generated artefacts.

> [!IMPORTANT]
> Content in this repository may include development, withdrawn, retired, and official releases. For normative use, always refer to the corresponding official buildingSMART publication.
> Files in this repository **should not be edited manually**, as any manual changes may be overwritten by subsequent automated updates.
> This repository is also **not the appropriate place to report issues, request changes, or propose corrections to the IFC specification**.

# IFC

This repository contains both the **automatically generated output of [`IFC4.x-development`](https://github.com/buildingSMART/IFC4.x-development) (DEV)**, and official release snapshots (RELEASE).

Official IFC publications are available from the [buildingSMART IFC Specifications Database](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/).

For specification issues and proposed changes, use the corresponding [`IFC4.x-development`](https://github.com/buildingSMART/IFC4.x-development) repository and its issue tracking process.

Normative and historical IFC releases, including downloadable packages and individual schema representations, are published at:

* [IFC Specifications Database](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)
* [IFC Release Notes](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ifc-release-notes/)
* [Official IFC Standards](https://standards.buildingsmart.org/IFC/)

## Version notation

```text
4.3.2.0 (example)
│ │ │ └─ Corrigendum
│ │ └─── Addendum
│ └───── Minor
└─────── Major
```

* **Major** - scope expansions or deletions that may introduce breaking changes.
* **Minor** - feature extensions. Compatibility is maintained for the core schema, but not necessarily for other definitions.
* **Addendum** - improvements to existing features. The schema may change while maintaining upward compatibility.
* **Corrigendum** - documentation improvements. The schema does not change, although deprecations may be introduced.

## Website deployment

The root `index.html` is the source template. File URLs may use globs in
their filenames, for example `IFC/DEV/IFC4_4/HTML/*.exp`. Keep directory paths
explicit. Each file URL on `standards.buildingsmart.org` (and each relative
file URL) must match exactly one file in the checkout. Zero or multiple matches
fail the build; directory URLs are assumed valid and external URLs are unchanged.
Only URLs in the root index are processed, not links inside generated publications.

To generate and validate a separate index locally:

```sh
python scripts/build_index.py --output /tmp/standards-index.html
```

The Pages workflow validates pull requests and deploys pushes to `main`, staging
the full static repository with the generated index and preserving `CNAME`.
In repository **Settings > Pages > Build and deployment**, set **Source** to
**GitHub Actions** instead of deploying from a branch. Build automation that pushes
publication updates must use credentials that trigger workflows (for example a
GitHub App token or PAT); pushes made with `GITHUB_TOKEN` do not trigger push workflows.

## License

Copyright © buildingSMART International Ltd. All Rights reserved until formal release. Final IFC is licensed under the **Creative Commons Attribution-NoDerivatives 4.0 International License (CC BY-ND 4.0)**.

