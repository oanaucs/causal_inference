import numpy as np

from scipy import stats


def test(x, y, z=None):

    df = len(x) - 2
    # print z.shape, len(z)
    if z is not None and z.shape[1] > 0:
        assert np.ndim(z) > 1
        df -= z.shape[1]
        beta_hat_x = np.linalg.lstsq(z, x, rcond=None)[0]
        xresid = x - np.dot(z, beta_hat_x)
        beta_hat_y = np.linalg.lstsq(z, y, rcond=None)[0]
        yresid = y - np.dot(z, beta_hat_y)
    else:
        xresid = x
        yresid = y
    
    value = np.corrcoef(xresid, yresid)[0,1]

    # Two-sided significance level
    trafo_val = value * np.sqrt(df / (1. - value**2))
    pval = stats.t.sf(np.abs(trafo_val), df) * 2

    return pval, value