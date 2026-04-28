# Changelog

## 0.1.0 (2026-04-28)

Full Changelog: [v0.0.4...v0.1.0](https://github.com/plazafyi/plaza-python/compare/v0.0.4...v0.1.0)

### Features

* **api:** api update ([24913e7](https://github.com/plazafyi/plaza-python/commit/24913e710835df35d4d180da21c9fb92e24ecd24))
* **api:** api update ([b1b08d8](https://github.com/plazafyi/plaza-python/commit/b1b08d86dafb1331a25cb587467b4eec5d485785))
* **api:** api update ([619765a](https://github.com/plazafyi/plaza-python/commit/619765ae5d9ae9a8e8398e77d3e60ebb5f079363))
* **api:** api update ([a720afe](https://github.com/plazafyi/plaza-python/commit/a720afe0af953e76b3daf7c8fc9fb8a1c266c574))
* **api:** api update ([145c32c](https://github.com/plazafyi/plaza-python/commit/145c32c2ba0a0d9eb020b01ed3ddc2a0973ec802))
* initial SDK generation ([c21a1a2](https://github.com/plazafyi/plaza-python/commit/c21a1a2310f05d76ff73b1f2ce2b6f976978644c))
* **internal:** implement indices array format for query and form serialization ([a7b4537](https://github.com/plazafyi/plaza-python/commit/a7b4537ca468a82e9db263f4a0ebe1029600f6c9))
* support setting headers via env ([428d39a](https://github.com/plazafyi/plaza-python/commit/428d39a082cd926a30a2524c70d9eda91aaea8e9))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([3725b86](https://github.com/plazafyi/plaza-python/commit/3725b863e6cd9cc5eec7e9add3150c33961bb9ee))
* ensure file data are only sent as 1 parameter ([b9cf08f](https://github.com/plazafyi/plaza-python/commit/b9cf08ffed884d055678589758b92863d3a94701))
* sanitize endpoint path params ([58a3626](https://github.com/plazafyi/plaza-python/commit/58a3626bcfc82582ff149d079dc5a30e9fe4905b))
* use correct field name format for multipart file arrays ([f82878e](https://github.com/plazafyi/plaza-python/commit/f82878e65c0d66e1104f2e1eaf337ce6a3235445))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([77135a3](https://github.com/plazafyi/plaza-python/commit/77135a3f3ee93154c3cb4cb5ccfbfc3a7cd3990b))


### Chores

* **ci:** skip lint on metadata-only changes ([5b32dcd](https://github.com/plazafyi/plaza-python/commit/5b32dcd2b2af1c8d4eb4777357e1db27dfc0a2f0))
* **internal:** more robust bootstrap script ([d57721e](https://github.com/plazafyi/plaza-python/commit/d57721e2813b27d742cdeeb34eff5e5147e5a36f))
* **internal:** update gitignore ([185db6e](https://github.com/plazafyi/plaza-python/commit/185db6eab87513661dff51b18b1fbe7ab00cdf2f))
* **tests:** bump steady to v0.19.4 ([e45807f](https://github.com/plazafyi/plaza-python/commit/e45807fbdf58ba22751056c92dd8e9ae5bb2a840))
* **tests:** bump steady to v0.19.5 ([8b17e4b](https://github.com/plazafyi/plaza-python/commit/8b17e4b82360e1df4ce0b1ab7800d9e22588b92e))
* **tests:** bump steady to v0.19.6 ([a91cd6c](https://github.com/plazafyi/plaza-python/commit/a91cd6cba5be9bd8c7108e90a8f80d108dae848f))
* **tests:** bump steady to v0.19.7 ([2a09f58](https://github.com/plazafyi/plaza-python/commit/2a09f58bfb273ec6b52a58f77649eabae206d41c))
* **tests:** bump steady to v0.20.1 ([d4f28b9](https://github.com/plazafyi/plaza-python/commit/d4f28b95cdd59aac63175f5ee768c4d499e102f6))
* **tests:** bump steady to v0.20.2 ([8a9a16f](https://github.com/plazafyi/plaza-python/commit/8a9a16f8613432ba8e37fc62cc850d78fd5011a3))
* **tests:** bump steady to v0.22.1 ([601ce8d](https://github.com/plazafyi/plaza-python/commit/601ce8daf7427828562a41c217ab26ca9ab46a83))


### Refactors

* **tests:** switch from prism to steady ([189166f](https://github.com/plazafyi/plaza-python/commit/189166f209b18840b20c15d16212ff61fb6de0c8))

## 0.0.4 (2026-03-19)

Full Changelog: [v0.0.3...v0.0.4](https://github.com/plazafyi/plaza-python/compare/v0.0.3...v0.0.4)

### Chores

* update SDK settings ([4542e6a](https://github.com/plazafyi/plaza-python/commit/4542e6a1346a1f0d97dff35cd915d52021e38b9c))
* update SDK settings ([4470813](https://github.com/plazafyi/plaza-python/commit/4470813c74bdb99e220f23e2dfc4ccb291dcfa33))

## 0.0.3 (2026-03-19)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/plazafyi/plaza-python/compare/v0.0.2...v0.0.3)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([50f2f86](https://github.com/plazafyi/plaza-python/commit/50f2f865b2e12b861d1471792556c37b260bf1b7))
* **pydantic:** do not pass `by_alias` unless set ([d76c5de](https://github.com/plazafyi/plaza-python/commit/d76c5ded1f1bc9cb0e17b939f89df78883f83702))


### Chores

* **internal:** tweak CI branches ([2a30d83](https://github.com/plazafyi/plaza-python/commit/2a30d8337e59b5f5ecadb06c88a5387d0a22025c))
* update SDK settings ([ff350db](https://github.com/plazafyi/plaza-python/commit/ff350db5850da19ca56bd5aed82c3ad36df560d2))
* update SDK settings ([3934323](https://github.com/plazafyi/plaza-python/commit/39343235fe15436b087e50c1e089d20e59129521))
* update SDK settings ([540054c](https://github.com/plazafyi/plaza-python/commit/540054c8241d3ac2833bc4dc61ad9cb5db79a50b))
* update SDK settings ([117f361](https://github.com/plazafyi/plaza-python/commit/117f36169b2b0422a201ff20fc767e955d9f22f5))

## 0.0.2 (2026-03-15)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/plazafyi/plaza-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([2647344](https://github.com/plazafyi/plaza-python/commit/26473449f53195ac16e2420c9f985176105edbbe))
* configure new SDK language ([eb10f9a](https://github.com/plazafyi/plaza-python/commit/eb10f9a7a2b062bc02d76ce2263eea19121e2c4c))
* update SDK settings ([2fa85be](https://github.com/plazafyi/plaza-python/commit/2fa85be6033f4436eef8b509489403dae170344e))
* update SDK settings ([acff344](https://github.com/plazafyi/plaza-python/commit/acff34420d9a474939b72b495eea1884ea3f0574))
