test:
	semgrep --validate --config=$$PWD/rules $$PWD
	semgrep --test --strict $$PWD
output:
	semgrep --test --strict --save-test-output-tar $$PWD
