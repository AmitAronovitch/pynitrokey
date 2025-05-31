from pynitrokey.helpers import b32padding


def test_b32padding():
    test_secrets = ['C' * n for n in range(30,40)]
    for secret in test_secrets:
        padded = b32padding(secret)
        n_pads = len(padded) - padded.rfind('C') - 1
        assert padded == secret + n_pads * '='
        assert len(padded) % 8 == 0
        assert 0 <= n_pads < 8
