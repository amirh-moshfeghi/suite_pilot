# :panda_face: eslint-config-mrmlnc

## Introduction

This is the ESLint configuration file used in [@mrmlnc](https://github.com/mrmlnc) projects. Based on [eslint-config-xo](https://github.com/xojs/eslint-config-xo).

Uses additional rules from:

* [`typescript-eslint`](https://github.com/typescript-eslint/typescript-eslint)
* [`eslint-plugin-import`](https://github.com/benmosher/eslint-plugin-import)
* [`eslint-plugin-mocha`](https://github.com/lo1tuma/eslint-plugin-mocha)
* [`eslint-plugin-node`](https://github.com/mysticatea/eslint-plugin-node)
* [`eslint-plugin-unicorn`](https://github.com/sindresorhus/eslint-plugin-unicorn)

Initially, this should work with TS code.

## Installation

```sh
npm install --save-dev eslint-config-mrmlnc
```

## Usage

Just extend `eslint-config-mrmlnc` in your [ESLint config](https://eslint.org/docs/user-guide/configuring) file, like so:

```json
{
	"extends": "eslint-config-mrmlnc"
}
```

Don't forget to override any rules if required.
