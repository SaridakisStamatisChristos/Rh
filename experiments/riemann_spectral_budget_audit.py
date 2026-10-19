"""Numerical diagnostic for the conditional Mobius-correlation spectral budget.

NOT a proof of RH, of the correlation-sign conjecture, or a rigorous
interval-arithmetic certification of zeta zeros/derivatives.

Requires: pip install mpmath
Usage: python riemann_spectral_budget_audit.py
"""
import mpmath as mp

mp.mp.dps = 35
budget = 6 / mp.pi**2
running = mp.mpf('0')
print('Conditional spectral budget 6/pi^2:', mp.nstr(budget, 15))
print('k    Im(rho_k)          pair_contribution       cumulative       fraction_of_budget')
for k in range(1, 51):
    rho = mp.zetazero(k)
    deriv = mp.diff(mp.zeta, rho)
    pair_contribution = 2 / abs(rho * deriv)**2
    running += pair_contribution
    if k in (1, 2, 5, 10, 15, 25, 50):
        print(f'{k:2d}   {mp.nstr(mp.im(rho), 14):>15}   '
              f'{mp.nstr(pair_contribution, 13):>18}   '
              f'{mp.nstr(running, 13):>14}   '
              f'{mp.nstr(running / budget, 10):>12}')
print('Unconditional lower bound from these pairs on limsup C(N)/log N:',
      mp.nstr((running - budget)/2, 15))
print('WARNING: Numbers are approximations, not certified enclosures.')