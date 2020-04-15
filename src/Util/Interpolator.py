import numpy as np


class Interpolator:

    @staticmethod
    def getInterpolatedValue(d, key):
        """

        :param d: Dictionary mapping numbers to numbers
        :param key: key within range of dictKeys
        :return: interpolated Value of dict keys
        """

        keys = Interpolator.__getKeyList__(d)

        valid_keys = Interpolator.__getValidKey__(keys, key)
        if np.abs(valid_keys[0] - valid_keys[1]) < 0.00000001:
            return d[valid_keys[0]]
        return Interpolator.__interpolate__(key, valid_keys, d)

    @staticmethod
    def getGradiant(d, key):
        keys = Interpolator.__getKeyList__(d)
        valid_keys = Interpolator.__getValidKey__(keys, key)
        if np.abs(valid_keys[0] - valid_keys[1]) < 0.00000001:
            return 0
        return (d[valid_keys[1]] - d[valid_keys[0]]) / (valid_keys[1] - valid_keys[0])

    @staticmethod
    def __getKeyList__(d):
        keys = []
        for k in d.keys():
            keys.append(k)
        keys.sort()
        return keys

    @staticmethod
    def __interpolate__(x, xv, d):
        y0 = d[xv[0]]
        y1 = d[xv[1]]
        return y0 + (y1 - y0) * (x - xv[0]) / (xv[1] - xv[0])

    @staticmethod
    def __getValidKey__(keys, key):
        keys.sort()
        key_max = max(keys)
        key_min = min(keys)
        if key <= key_min:
            return key_min, key_min
        if key >= key_max:
            return key_max, key_max

        key0 = 0
        key1 = 0

        for k in keys:
            if key == k:
                return key, key

        i = 0
        for k in keys:
            if key < k:
                key1 = keys[i]
                break
            i = i + 1

        i = len(keys) - 1
        for k in reversed(keys):
            if key > k:
                key0 = keys[i]
                break
            i = i - 1

        return key0, key1


def main():
    """
    Demo and Test for this class.
    :return: None
    """
    cw = {0.1: 0.5096, 0.5: 0.4227, 0.75: 0.4073}  # just an example dict. implement file-reader later
    other = {0.2: 20, 0.6: 60, 0.1: 10, 0: 0, 1: 100}

    d = other
    x = 0.76478
    print("")
    print("x:", 5 * "\t", x)
    print("keys:", 4 * "\t", Interpolator.__getKeyList__(d))
    print("valid Keys:", 2 * "\t", Interpolator.__getValidKey__(Interpolator.__getKeyList__(d), x))
    print("interpolated value:\t", Interpolator.getInterpolatedValue(d, x))


# run demo
if __name__ == '__main__':
    main()
