# Template repo

This repository can be used to start building your own vocabulary in a way that is compatible with the github actions as defined in `.github/workflows`.
For instructions on [how to create a repo from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

# .github
This folder contains the `ISSUE TEMPLATES` to add, modify or deprecate a vocabulary term as well as the config files to configure actions (`.github/workflows`).

# Data
Add the vocabulary content as `.csv` and/or `.yaml` depending on the reusable workflows you want to use.

# Rules
The `voc2skosmos` workflow that transforms a `.csv` into a SKOS vocabulary requires a set of `yarrml` rules.

# Schema
Contains the data schema for the vocabulary terms and the changelog schema. Note that the workflows implemented within the eu-parc repository also support the usage of a uri to point to a data schema.

# Changelog
The changelog should be used as an instrument to keep track of changes to the vocabulary in between releases. The changelog should be updated with each pull request.
[NOTE: The changelog schema will be deprecated soon. We'll transform the workflows to simply use diffs of the released versions.]

# Workflows
* Add identifiers:
* Publish Vocabulary: Two options (code for both hosted at [voc2skosmos-workflow](https://github.com/eu-parc/voc2skosmos-workflow))
    * csv2skos: requires a `.csv` file in the data: 
    * yml2skos: requires a `.yml` file made according to a LinkML schema: 
* [voc2nanopub](https://github.com/eu-parc/voc2nanopub): Not configured in the template but departs from the same LinkML-based `.yml`

# Building vocabularies with LinkML
* [LinkML documentation](https://linkml.io/linkml/)
* Example: [matrix-vocabulary](https://github.com/eu-parc/matrix-vocabulary)
