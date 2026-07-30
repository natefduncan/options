# options

Options pricing and volatility analysis from the terminal.

Define a position as a TOML file, then plot its payoff at expiration or sweep any
Black-Scholes input against any output — all rendered as ASCII charts, no notebook or
GUI required.

## Install

```bash
pip install -e .
```

## Define a position

A position is a title plus one or more contracts:

```toml
title = "Long Straddle"

[[contracts]]
type = "Call"
position = "BUY"
price = 5
expiration = "2023-01-01"
strike = 40

[[contracts]]
type = "Put"
position = "BUY"
price = 5
expiration = "2023-01-01"
strike = 40
```

`type` is `Call` or `Put`; `position` is `BUY` or `SELL`. Ten common structures ship in
`strategies/` — long and short calls, puts, straddles, strangles, and butterflies.

## Usage

Plot the payoff diagram at expiration:

```bash
options parity-graph strategies/long_straddle.toml --underlying-max 100
```

Sweep one Black-Scholes input against one output across the whole position:

```bash
options info-graph strategies/long_call.toml -x volatility -y contract_price
```

Both axes accept any of:

- **Inputs:** `underlying_price`, `expiration`, `volatility`, `interest`
- **Outputs:** `contract_price`, `delta`, `gamma`, `theta`, `vega`, `rho`

So `-x underlying_price -y delta` traces the delta curve of the combined position;
`-x volatility -y contract_price` traces its vega exposure.

## What's implemented

`options/pricing.py` is a from-scratch Black-Scholes implementation — prices and the
full first- and second-order Greeks for both calls and puts, using only the standard
library. `options/portfolio.py` aggregates across every contract in a position, so the
curves reflect the whole structure rather than a single leg.

## License

See `LICENSE`.
