import protocol


rb = protocol.RockBlock("/dev/serial0")


while True:
    a = rb.check_connection()
    if a > 0:
        rb.send_message("testing")
    print a
