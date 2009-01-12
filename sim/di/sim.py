from devlib.DeviceInterface import DevIf, EndPoint, Register

di=DevIf(name='Devices', 
         comment='My Test Device List', 
         endpoint_list=[
    EndPoint(name='XEM3010',
             comment='Opal Kelly XEM 3010',
             regAddrWidth=16, 
             regDataWidth=16,
             register_list=[
        Register(name='buttons',
                type='int',
                mode='volatile',
                access='ro',
                width=2,
                comment='button state'),
        Register(name='led0', 
                 type='int',
                 mode='static',
                 access='rw',
                 width=8,
                 comment='When led0 is selected, this drives the leds',
          init=85,
        ),
        Register(name='counter',
                 type='int',
                 mode='volatile',
                 access='ro',
                 width=16,
                 comment="A counter")
    ])])

