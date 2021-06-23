module.exports = {
  testEnvironment: 'node',
  moduleFileExtensions: [
    "js",
    "jsx",
    "json",
    "node",
  ],
  testRegex: '(/__tests__/.*|(\\.|/)(test|spec))\\.(js)x?$',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  "collectCoverageFrom": [
    "**/*.{js,jsx}",
    "!**/node_modules/**",
    "!**/coverage/**",
    "!**/vendor/**",
    "!jest.config.js"
  ]
};