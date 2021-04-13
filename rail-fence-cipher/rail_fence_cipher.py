import toolz


def encode(message, rails):
    encoded = []

    for i in range(rails):
        if i == 0 or i == rails - 1:
            encoded.append(message[i :: 2 * rails - 2])
        else:
            l1 = message[i :: 2 * rails - 2]
            l2 = message[2 * rails - (i + 2) :: 2 * rails - 2]
            encoded.append("".join(toolz.interleave([l1, l2])))

    return "".join(encoded)


def decode(encoded_message, rails):
    decoded = []
    return decoded
