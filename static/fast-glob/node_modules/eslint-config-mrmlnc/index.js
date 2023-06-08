const XO_RULES_OVERRIDES = {
	'arrow-parens': [
		'error',
		'always'
	],
	'object-curly-spacing': [
		'error',
		'always'
	],
	'linebreak-style': [
		'error',
		'unix'
	],
	'valid-jsdoc': 'off',
	'lines-between-class-members': [
		'error',
		'always',
		{
			exceptAfterSingleLine: true
		}
	],
	'prefer-destructuring': 'off'
};

const IMPORT_RULES = {
	'import/no-unresolved': [
		'error',
		{
			caseSensitive: true
		}
	],
	'import/named': 'error',
	'import/default': 'error',
	'import/namespace': [
		'error',
		{
			allowComputed: true
		}
	],
	'import/no-absolute-path': 'error',
	'import/no-dynamic-require': 'error',
	'import/no-webpack-loader-syntax': 'error',
	'import/no-self-import': 'error',
	'import/no-useless-path-segments': [
		'error',
		{
			noUselessIndex: true
		}
	],
	'import/export': 'error',
	'import/no-named-as-default': 'error',
	'import/no-named-as-default-member': 'error',
	'import/no-deprecated': 'warn',
	'import/no-extraneous-dependencies': 'error',
	'import/no-mutable-exports': 'error',
	'import/no-unused-modules': 'error',
	'import/no-commonjs': 'error',
	'import/no-amd': 'error',
	'import/first': 'error',
	'import/no-duplicates': 'error',
	'import/extensions': [
		'error',
		'never',
		{
			json: 'always'
		}
	],
	'import/order': 'error',
	'import/newline-after-import': 'error',
	'import/no-unassigned-import': 'error',
	'import/no-named-default': 'error'
};

const NODE_RULES = {
	'node/no-unpublished-bin': 'error',
	'node/process-exit-as-throw': 'error',
	'node/no-deprecated-api': 'error',
	'node/prefer-global/buffer': [
		'error',
		'always'
	],
	'node/prefer-global/console': [
		'error',
		'always'
	],
	'node/prefer-global/process': [
		'error',
		'always'
	],
	'node/no-exports-assign': 'error'
};

const UNICORN_RULES = {
	'unicorn/catch-error-name': [
		'error',
		{
			name: 'error'
		}
	],
	'unicorn/custom-error-definition': 'error',
	'unicorn/error-message': 'error',
	'unicorn/escape-case': 'error',
	'unicorn/explicit-length-check': 'error',
	'unicorn/filename-case': [
		'error',
		{
			case: 'kebabCase'
		}
	],
	'unicorn/import-index': 'error',
	'unicorn/new-for-builtins': 'error',
	'unicorn/no-abusive-eslint-disable': 'error',
	'unicorn/no-array-instanceof': 'error',
	'unicorn/no-console-spaces': 'error',
	'unicorn/no-fn-reference-in-iterator': 'off',
	'unicorn/no-for-loop': 'error',
	'unicorn/no-hex-escape': 'error',
	'unicorn/no-keyword-prefix': 'off',
	'unicorn/no-nested-ternary': 'error',
	'unicorn/no-new-buffer': 'error',
	'unicorn/no-unreadable-array-destructuring': 'error',
	'unicorn/no-unsafe-regex': 'error',
	'unicorn/no-unused-properties': 'error',
	'unicorn/no-zero-fractions': 'error',
	'unicorn/number-literal-case': 'error',
	'unicorn/prefer-event-key': 'error',
	'unicorn/prefer-exponentiation-operator': 'error',
	'unicorn/prefer-flat-map': 'error',
	'unicorn/prefer-includes': 'error',
	'unicorn/prefer-negative-index': 'error',
	'unicorn/prefer-spread': 'error',
	'unicorn/prefer-starts-ends-with': 'error',
	'unicorn/prefer-string-slice': 'error',
	'unicorn/prefer-trim-start-end': 'error',
	'unicorn/prefer-type-error': 'error',
	'unicorn/prevent-abbreviations': [
		'error',
		{
			whitelist: {
				args: true
			}
		}
	],
	'unicorn/regex-shorthand': 'error',
	'unicorn/throw-new-error': 'error'
};

const TYPESCRIPT_ESLINT_RULES = {
	// https://github.com/typescript-eslint/typescript-eslint/issues/239
	'no-inner-declarations': 'off',
	'@typescript-eslint/adjacent-overload-signatures': 'error',
	'@typescript-eslint/array-type': [
		'error',
		{
			default: 'array-simple'
		}
	],
	'@typescript-eslint/await-thenable': 'error',
	'@typescript-eslint/ban-ts-ignore': 'error',
	'@typescript-eslint/ban-types': [
		'error',
		{
			types: {
				String: {
					message: 'Use `string` instead.',
					fixWith: 'string'
				},
				Number: {
					message: 'Use `number` instead.',
					fixWith: 'number'
				},
				Boolean: {
					message: 'Use `boolean` instead.',
					fixWith: 'boolean'
				},
				Symbol: {
					message: 'Use `symbol` instead.',
					fixWith: 'symbol'
				},
				Object: {
					message: 'Use `object` instead.',
					fixWith: 'object'
				},
				object: 'Use `{}` instead.',
				Function: 'Use a specific function type instead, like `() => void`.'
			}
		}
	],
	'@typescript-eslint/camelcase': [
		'error',
		{
			properties: 'always',
			ignoreDestructuring: false
		}
	],
	'@typescript-eslint/class-name-casing': 'error',
	'@typescript-eslint/consistent-type-assertions': [
		'error',
		{
			assertionStyle: 'as',
			objectLiteralTypeAssertions: 'never'
		}
	],
	'@typescript-eslint/consistent-type-definitions': [
		'error',
		'type'
	],
	'@typescript-eslint/explicit-function-return-type': [
		'error',
		{
			allowExpressions: true,
			allowTypedFunctionExpressions: true,
			allowHigherOrderFunctions: true
		}
	],
	'@typescript-eslint/explicit-member-accessibility': [
		'error',
		{
			accessibility: 'explicit',
			overrides: {
				constructors: 'off'
			}
		}
	],
	'func-call-spacing': 'off',
	'@typescript-eslint/func-call-spacing': [
		'error',
		'never'
	],
	'@typescript-eslint/generic-type-naming': [
		'error',
		'^T$|^T[A-Z][a-zA-Z]+$'
	],
	indent: 'off',
	'@typescript-eslint/indent': [
		'error',
		'tab',
		{
			SwitchCase: 1
		}
	],
	'@typescript-eslint/interface-name-prefix': [
		'error',
		{
			prefixWithI: 'never'
		}
	],
	'@typescript-eslint/member-delimiter-style': [
		'error',
		{
			multiline: {
				delimiter: 'semi',
				requireLast: true
			},
			singleline: {
				delimiter: 'semi',
				requireLast: false
			}
		}
	],
	'@typescript-eslint/member-naming': [
		'error',
		{
			private: '^_'
		}
	],
	'@typescript-eslint/member-ordering': [
		'error',
		{
			default: [
				'static-field',
				'instance-field',
				'constructor',
				'static-method',
				'instance-method'
			],
			interfaces: [
				'constructor',
				'method',
				'field'
			],
			typeLiterals: [
				'constructor',
				'method',
				'field'
			]
		}
	],
	'no-array-constructor': 'off',
	'@typescript-eslint/no-array-constructor': 'error',
	'@typescript-eslint/no-dynamic-delete': 'error',
	'no-empty-function': 'off',
	'@typescript-eslint/no-empty-function': 'error',
	'@typescript-eslint/no-empty-interface': [
		'error',
		{
			allowSingleExtends: false
		}
	],
	'@typescript-eslint/no-explicit-any': [
		'error',
		{
			fixToUnknown: true
		}
	],
	'@typescript-eslint/no-extra-non-null-assertion': 'error',
	'no-extra-parens': 'off',
	'@typescript-eslint/no-extra-parens': 'error',
	'no-extra-semi': 'off',
	'@typescript-eslint/no-extra-semi': 'error',
	'@typescript-eslint/no-extraneous-class': 'error',
	'@typescript-eslint/no-floating-promises': 'error',
	'@typescript-eslint/no-for-in-array': 'error',
	'@typescript-eslint/no-inferrable-types': [
		'error',
		{
			ignoreParameters: true,
			ignoreProperties: true
		}
	],
	'no-magic-numbers': 'off',
	'@typescript-eslint/no-magic-numbers': [
		'error',
		{
			ignore: [
				0,
				1
			],
			ignoreEnums: true,
			ignoreNumericLiteralTypes: true,
			ignoreReadonlyClassProperties: true
		}
	],
	'@typescript-eslint/no-misused-new': 'error',
	'@typescript-eslint/no-misused-promises': [
		'error',
		{
			checksVoidReturn: true,
			checksConditionals: true
		}
	],
	// I don't know why, but this rule enable by default
	'@typescript-eslint/no-namespace': 'off',
	'@typescript-eslint/no-non-null-assertion': 'error',
	'@typescript-eslint/no-require-imports': 'error',
	'@typescript-eslint/no-this-alias': 'error',
	'@typescript-eslint/no-throw-literal': 'error',
	'@typescript-eslint/no-unnecessary-qualifier': 'error',
	'@typescript-eslint/no-unnecessary-type-arguments': 'error',
	'@typescript-eslint/no-unnecessary-type-assertion': 'error',
	'no-unused-vars': 'off',
	'@typescript-eslint/no-unused-vars': [
		'error',
		{
			vars: 'all',
			args: 'after-used',
			argsIgnorePattern: '^_',
			caughtErrors: 'all',
			caughtErrorsIgnorePattern: '^_$'
		}
	],
	'no-use-before-define': 'off',
	'@typescript-eslint/no-use-before-define': [
		'error',
		{
			functions: false
		}
	],
	'no-useless-constructor': 'off',
	'@typescript-eslint/no-useless-constructor': 'error',
	'@typescript-eslint/no-var-requires': 'error',
	'@typescript-eslint/prefer-for-of': 'error',
	'@typescript-eslint/prefer-function-type': 'error',
	'@typescript-eslint/prefer-includes': 'error',
	'@typescript-eslint/prefer-namespace-keyword': 'error',
	'@typescript-eslint/prefer-nullish-coalescing': [
		'error',
		{
			ignoreConditionalTests: true,
			ignoreMixedLogicalExpressions: true
		}
	],
	'@typescript-eslint/prefer-optional-chain': 'error',
	'@typescript-eslint/prefer-readonly': 'error',
	'@typescript-eslint/prefer-regexp-exec': 'error',
	'@typescript-eslint/prefer-string-starts-ends-with': 'error',
	quotes: 'off',
	'@typescript-eslint/quotes': [
		'error',
		'single',
		{
			avoidEscape: true
		}
	],
	'@typescript-eslint/require-array-sort-compare': 'error',
	'require-await': 'off',
	'@typescript-eslint/require-await': 'error',
	'@typescript-eslint/restrict-plus-operands': 'error',
	'@typescript-eslint/return-await': [
		'error',
		'in-try-catch'
	],
	semi: 'off',
	'@typescript-eslint/semi': [
		'error',
		'always'
	],
	'space-before-function-paren': 'off',
	'@typescript-eslint/space-before-function-paren': [
		'error',
		{
			anonymous: 'always',
			named: 'never',
			asyncArrow: 'always'
		}
	],
	'@typescript-eslint/strict-boolean-expressions': [
		'error',
		{
			ignoreRhs: true
		}
	],
	'@typescript-eslint/no-unnecessary-condition': [
		'error',
		{
			ignoreRhs: true
		}
	],
	'@typescript-eslint/triple-slash-reference': 'error',
	'@typescript-eslint/type-annotation-spacing': [
		'error',
		{
			before: false,
			after: true,
			overrides: {
				arrow: {
					before: true,
					after: true
				}
			}
		}
	],
	'@typescript-eslint/typedef': [
		'error',
		{
			arrowParameter: false,
			memberVariableDeclaration: true,
			parameter: true,
			propertyDeclaration: true
		}
	],
	'@typescript-eslint/unified-signatures': 'error'
};

const MOCHA_RULES = {
	'mocha/handle-done-callback': 'error',
	'mocha/max-top-level-suites': [
		'error',
		{
			limit: 3
		}
	],
	'mocha/no-async-describe': 'error',
	'mocha/no-exclusive-tests': 'error',
	'mocha/no-global-tests': 'error',
	'mocha/no-identical-title': 'error',
	'mocha/no-nested-tests': 'error',
	'mocha/no-pending-tests': 'error',
	'mocha/no-return-and-callback': 'error',
	'mocha/no-return-from-async': 'error',
	'mocha/no-skipped-tests': 'error',
	'mocha/prefer-arrow-callback': [
		'error',
		{
			allowNamedFunctions: true
		}
	]
};

// eslint-disable-next-line import/no-commonjs
module.exports = {
	extends: 'xo/esnext',
	// eslint-disable-next-line unicorn/prevent-abbreviations
	env: {
		node: true,
		es6: true,
		mocha: true
	},
	parserOptions: {
		ecmaVersion: 2020,
		sourceType: 'module'
	},
	plugins: [
		'import',
		'node',
		'unicorn'
	],
	rules: {
		...XO_RULES_OVERRIDES,
		...IMPORT_RULES,
		...NODE_RULES,
		...UNICORN_RULES
	},
	overrides: [
		{
			files: [
				'**/*.ts'
			],
			extends: [
				'plugin:@typescript-eslint/recommended'
			],
			parserOptions: {
				project: 'tsconfig.json'
			},
			parser: '@typescript-eslint/parser',
			settings: {
				'import/extensions': [
					'.js',
					'.jsx',
					'.ts',
					'.tsx'
				],
				'import/resolver': {
					node: {
						extensions: [
							'.js',
							'.jsx',
							'.ts',
							'.tsx'
						]
					}
				},
				'import/parsers': {
					'@typescript-eslint/parser': [
						'.ts',
						'.tsx'
					]
				}
			},
			plugins: [
				'@typescript-eslint'
			],
			rules: {
				...TYPESCRIPT_ESLINT_RULES
			}
		},
		{
			files: [
				'**/*.spec.ts'
			],
			plugins: [
				'mocha'
			],
			rules: {
				'max-nested-callbacks': 'off',
				'@typescript-eslint/no-magic-numbers': 'off',
				...MOCHA_RULES
			}
		}
	]
};
