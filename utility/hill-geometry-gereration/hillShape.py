import numpy as np

def profile(yy):
    'Calculate the shape of the periodic hill'

    import numpy as np

    y = np.array(yy)
    x = y * 28

    h = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] > 126.0 :
            x[i] = 252.0 - x[i]

        if (x[i]>=0) and (x[i]<9) :
            h[i] = np.minimum(28., 2.8e+01 + 0.0e+00*x[i] + \
                              6.775070969851e-03*x[i]**2 - 2.124527775800e-03*x[i]**3);
        elif (x[i]>=9) and (x[i]<14) :
            h[i] = 2.507355893131E+01 + 9.754803562315E-01*x[i] - \
                   1.016116352781E-01*x[i]**2 + 1.889794677828E-03*x[i]**3;
        elif (x[i]>=14) and (x[i]<20) :
            h[i] = 2.579601052357E+01 + 8.206693007457E-01*x[i] - \
                   9.055370274339E-02*x[i]**2 + 1.626510569859E-03*x[i]**3;
        elif (x[i]>=20) and (x[i]<30) :
            h[i] = 4.046435022819E+01 - 1.379581654948E+00*x[i] + \
                   1.945884504128E-02*x[i]**2 - 2.070318932190E-04*x[i]**3;
        elif (x[i]>=30) and (x[i]<40) :
            h[i] = 1.792461334664E+01 + 8.743920332081E-01*x[i] - \
                   5.567361123058E-02*x[i]**2 + 6.277731764683E-04*x[i]**3;
        elif (x[i]>=40) and (x[i]<=54) :
            h[i] = np.maximum(0., 5.639011190988E+01 - 2.010520359035E+00*x[i] + \
                              1.644919857549E-02*x[i]**2 + 2.674976141766E-05*x[i]**3);
        elif (x[i]>54) and (x[i]<=126) :
            h[i] = 0;

    hout = h/28.0
    return hout


def para_profile(yy, a):
    'Calculate the shape of the parameterized periodic hill'

    import numpy as np

    y = np.array(yy)
    x = y * 28
    ya = y

    h = np.zeros(len(x))

    # Must appear before the x[i] is revised in next for loop
    for i in range(len(x)):
        if (x[i]>=0) and (x[i]<54) :
            ya[i] *= a
        elif (x[i]>54) and (x[i]<=126) :
            ya[i] -= (54/28.0*(1-a))
        elif (x[i]>126) and (x[i]<=198) :
            ya[i] -= (54/28.0*(1-a))
        elif (x[i]>198) and (x[i]<=252) :
            ya[i] -= (54/28.0*(1-a))
            ya[i] -= (x[i]-198)*(1-a)/28.0
    
    for i in range(len(x)):
        if x[i] > 126.0 :
            x[i] = 252.0 - x[i]

        if (x[i]>=0) and (x[i]<9) :
            h[i] = np.minimum(28., 2.8e+01 + 0.0e+00*x[i] + \
                              6.775070969851e-03*x[i]**2 - 2.124527775800e-03*x[i]**3);
        elif (x[i]>=9) and (x[i]<14) :
            h[i] = 2.507355893131E+01 + 9.754803562315E-01*x[i] - \
                   1.016116352781E-01*x[i]**2 + 1.889794677828E-03*x[i]**3;
        elif (x[i]>=14) and (x[i]<20) :
            h[i] = 2.579601052357E+01 + 8.206693007457E-01*x[i] - \
                   9.055370274339E-02*x[i]**2 + 1.626510569859E-03*x[i]**3;
        elif (x[i]>=20) and (x[i]<30) :
            h[i] = 4.046435022819E+01 - 1.379581654948E+00*x[i] + \
                   1.945884504128E-02*x[i]**2 - 2.070318932190E-04*x[i]**3;
        elif (x[i]>=30) and (x[i]<40) :
            h[i] = 1.792461334664E+01 + 8.743920332081E-01*x[i] - \
                   5.567361123058E-02*x[i]**2 + 6.277731764683E-04*x[i]**3;
        elif (x[i]>=40) and (x[i]<=54) :
            h[i] = np.maximum(0., 5.639011190988E+01 - 2.010520359035E+00*x[i] + \
                              1.644919857549E-02*x[i]**2 + 2.674976141766E-05*x[i]**3);
        elif (x[i]>54) and (x[i]<=126) :
            h[i] = 0;


    hout = h/28.0
    return ya, hout



if __name__ == "__main__":
        
    import matplotlib.pyplot as plt
    yy=np.arange(0, 9, 0.01)
    
    h = profile(yy)
    ya1, h0p5 = para_profile(yy, 0.5)
    ya2, h1p5 = para_profile(yy, 1.5)

    a=0.5

    symbols=['k-', 'g-', 'b-', 'm-', 'r-']
    alphas = np.array([0.5, 0.8, 1, 1.2, 1.5])
    
    for i, a in enumerate(alphas):
    
        ya, ha = para_profile(yy, a)
        plt.plot(ya, ha, symbols[i])
        xend = ya[-1]
        outline = np.array([[0, 0, xend, xend], [1, 3.06, 3.06, 1]])
        plt.plot(outline[0, :], outline[1, :], symbols[i])

    plt.axis([0, 5, 0, 5])
    plt.axis('equal')
    plt.savefig('para-shapes.pdf')
    plt.show()
