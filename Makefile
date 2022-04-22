test:
	semgrep --validate --config=./rules ./rules
	semgrep --test --strict ./rules
output:
	semgrep --test --strict --save-test-output-tar ./rules
