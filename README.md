# template-rules
[![powered by semgrep](https://img.shields.io/badge/powered%20by-semgrep-1B2F3D?labelColor=lightgrey&link=https://semgrep.dev/&style=flat-square&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA0AAAAOCAYAAAD0f5bSAAAABmJLR0QA/gD+AP+cH+QUAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH5AYMEy0l8dkqrQAAAvFJREFUKBUB5gIZ/QEAAP8BAAAAAAMG6AD9+hn/GzA//wD//wAAAAD+AAAAAgABAQDl0MEBAwbmAf36GQAAAAAAAQEC9QH//gv/Gi1GFQEC+OoAAAAAAAAAAAABAQAA//8AAAAAAAAAAAD//ggX5tO66gID9AEBFSRxAgYLzRQAAADpAAAAAP7+/gDl0cMPAAAA+wAAAPkbLz39AgICAAAAAAAAAAAs+vU12AEbLz4bAAAA5P8AAAAA//4A5NDDEwEBAO///wABAQEAAP//ABwcMD7hAQEBAAAAAAAAAAAaAgAAAOAAAAAAAQEBAOXRwxUAAADw//8AAgAAAAD//wAAAAAA5OXRwhcAAQEAAAAAAAAAAOICAAAABP3+/gDjzsAT//8A7gAAAAEAAAD+AAAA/wAAAAAAAAAA//8A7ePOwA/+/v4AAAAABAIAAAAAAAAAAAAAAO8AAAABAAAAAAAAAAIAAAABAAAAAAAAAAgAAAD/AAAA8wAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAA8AAAAEAAAA/gAAAP8AAAADAAAA/gAAAP8AAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAA7wAAAPsAAAARAAAABAAAAP4AAAAAAAAAAgAAABYAAAAAAAAAAAIAAAD8AwICAB0yQP78/v4GAAAA/wAAAPAAAAD9AAAA/wAAAPr9//8aHTJA6AICAgAAAAD8AgAAADIAAAAAAP//AB4wPvgAAAARAQEA/gEBAP4BAQABAAAAGB0vPeIA//8AAAAAAAAAABAC+vUz1QAAAA8AAAAAAwMDABwwPu3//wAe//8AAv//ABAcMD7lAwMDAAAAAAAAAAAG+vU0+QEBAvUB//4L/xotRhUBAvjqAAAAAAAAAAAAAQEAAP//AAAAAAAAAAAA//4IF+bTuuoCA/QBAQAA/wEAAAAAAwboAP36Gf8bMD//AP//AAAAAP4AAAACAAEBAOXQwQEDBuYB/foZAAAAAAD4I6qbK3+1zQAAAABJRU5ErkJggg==)](https://semgrep.dev/)
[![r2c community slack](https://img.shields.io/badge/slack-join-green?style=flat-square)](https://r2c.dev/slack)

a template repo for semgrep rules and semgrep performance.

## Geting started

This guide assumes you are familiar with [Semgrep](https://semgrep.dev/docs) and have it already installed.

1. Test out this template repo with the following command:

```bash
git clone clone https://github.com/semgrep/template-rules.git
```

To test out the rules template, run:

```bash
semgrep --config template-rules/rules template-rules/rules/hello-world.py
```

To test out the benchmarking scripts in `semgrep/perf`, run:
```bash
cd semgrep/perf
make
```
or refer to https://github.com/returntocorp/semgrep/tree/develop/perf. 

2. Copy this template to your own repo.

## Performance CI Configurations

---

### What are these for?
These configurations are Github Action scripts that you can run in CI. You can find them in `perf-templates`. 

**benchmark-tests.yml**
`benchmark-tests.yml` is a YAML file that runs the timing benchmark with source code in [perf](https://github.com/returntocorp/semgrep/tree/develop/perf). 

The `Run Timing Benchmark With Latest Semgrep Version` action runs the benchmark script with the following flags:
- `--small-only`: runs the script on small benchmarking repositories only, as compared to medium-sized or large-sized repositories.
- `--std-only`: runs semgrep with no optimization flags.
- `--output-time-per-rule-json`: outputs a JSON file that states the total time taken per rule per repository and the average time taken per rule.

The `Run Timing Benchmark With Specified Config File` action runs the benchmark script with the additional flag:
- `--config`: runs the benchmarking script using the repositories and rules specified in a YAML config file.

**config-template.yml**
`config-template.yml` is a YAML file that lets the user specify which repositories and rules to run the benchmarking scripts on. Feeding this file into the `--config` flag for the `run-benchmarks` script in the `semgrep/perf` folder.

### How can I use these?
1. Copy the desired configuration files into your `.github/workflows` folder. 
2. Change these configuration templates as needed.
3. Create a pull request with these changes and see if the appropriate tests are running in your Github Actions!

## Rule Templates

1. Add your rules (and their test files) to the `rules` folder
2. Iterate rules and ensure they pass the built-in tests
3. Open a PR to the [Awesome Semgrep](https://github.com/returntocorp/semgrep-docs/docs/awesome.md) list
4. Ask for help in the Semgrep [community slack](https://r2c.dev/slack) any time 👋
