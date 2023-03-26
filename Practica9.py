print("---Introduce el tipo de conversión---")
print("1. Monedas")
print("2. Longitud")
print("3. Masa")
print("4. Almacenamiento")
print("5. Tiempo")
print("6. Volumen")
print("7. Área")
print("8. Manzanas")
print("9. Hectareas")
type_operacion = (input(''))

if type_operacion == '1':
    bel_cost = float(277.62891)
    bel_dol = float(0.50)
    bel_quet = float(3.8755373)
    bel_lemp = float(12.224747)
    bel_cord = float(18.058015)
    bel_balb = float(0.49615876)

    cost_bel = float(0.0036035764)
    cost_dol = float(0.0017879295)
    cost_quet = float(0.013963461)
    cost_lemp = float(0.044074632)
    cost_cord = float(0.065076038)
    cost_balb = float(0.0017880506)

    dol_cost = float(559.23774)
    dol_bel = float(2.0155122)
    dol_quet = float(7.8095608)
    dol_lemp = float(24.654581)
    dol_cord = float(36.395011)
    dol_balb = float(1.0)

    quet_bel = float(0.25808622)
    quet_cost = float(71.648992)
    quet_dol = float(0.1280494)
    quet_lemp = float(3.1571134)
    quet_cord = float(4.6603531)
    quet_balb = float(0.1280494)

    lemp_bel = float(0.081774699)
    lemp_cost = float(22.69735)
    lemp_dol = float(0.040570282)
    lemp_quet = float(0.31685658)
    lemp_cord = float(1.4765571)
    lemp_balb = float(0.040564496)

    cord_bel = float(0.055378583)
    cord_cost = float(15.36759)
    cord_dol = float(0.027476275)
    cord_quet = float(0.21458341)
    cord_lemp = float(0.67739848)
    cord_balb = float(0.027476323)

    balb_cost = float(559.23774)
    balb_bel = float(2.0155122)
    balb_dol = float(1.0)
    balb_quet = float(7.8095608)
    balb_lemp = float(24.654581)
    balb_cord = float(36.395011)

    print("---Conversiones de Monedas:---")
    print("¿Qué moneda desea convertir?")
    print("1. Dolar Beliceño - Belice")
    print("2. Colon costarricence - Costa Rica")
    print("3. Dolar Estadounidense - Estados Unidos")
    print("4. Quétzal - Guatemala")
    print("5. Lempira - Honduras")
    print("6. Cordoba - Nicaragua")
    print("7. Balboa - panama")  
    type_moneda = (input('')) 
    print("---Ingrese el valor de la moneda seleccionada:---")
    val_mon1 = (float(input("")))

    if type_moneda == '1':
        print("---¿A qué moneda desea convertir?---")
        print("1. Colon costarricence - Costa Rica")
        print("2. Dolar Estadounidense - Estados Unidos")
        print("3. Quétzal - Guatemala")
        print("4. Lempira - Honduras")
        print("5. Cordoba - Nicaragua")
        print("6. Balboa - panama") 
        type_conver = (input(""))


        if type_conver == '1':
            result = (val_mon1 * bel_cost)
        elif type_conver == '2':
            result = (val_mon1 * bel_dol)
        elif type_conver == '3':
            result = (val_mon1 * bel_quet)
        elif type_conver == '4':
            result = (val_mon1 * bel_lemp)  
        elif type_conver == '5':   
            result = (val_mon1 * bel_cord)
        elif type_conver == '6':
            result = (val_mon1 * bel_balb)        
        else:
            print("Valor invalido")
    elif type_moneda == '2':
        print(" ")
        print("¿---A qué moneda desea convertir?---")
        print("1. Dolar Beliceño - Belice")
        print("2. Dolar Estadounidense - Estados Unidos")
        print("3. Quétzal - Guatemala")
        print("4. Lempira - Honduras")
        print("5. Cordoba - Nicaragua")
        print("6. Balboa - panama") 
        type_conver = (input(""))
        print(" ")

        if type_conver == '1':
            result = (val_mon1 * cost_bel)
        elif type_conver == '2':
            result = (val_mon1 * cost_dol)
        elif type_conver == '3':
            result = (val_mon1 * cost_quet)
        elif type_conver == '4':
            result = (val_mon1 * cost_lemp)
        elif type_conver == '5':
            result = (val_mon1 * cost_cord)
        elif type_conver == '6':
            result = (val_mon1 * cost_balb)
        else:
            print("Valor invalido")
    elif type_moneda == '3':
        print("¿---A qué moneda desea convertir?---")
        print("1. Dolar Beliceño - Belice")
        print("2. Colon costarricence - Costa Rica")
        print("3. Quétzal - Guatemala")
        print("4. Lempira - Honduras")
        print("5. Cordoba - Nicaragua")
        print("6. Balboa - panama")  
        type_conver = (input(''))
        
        if type_conver == '1':
            result = (val_mon1 * dol_bel)
        elif type_conver == '2':
            result = (val_mon1 * dol_cost)
        elif type_conver == '3':
            result = (val_mon1 * dol_quet)
        elif type_conver == '4':
            result = (val_mon1 * dol_lemp)
        elif type_conver == '5':
            result = (val_mon1 * dol_cord)
        elif type_conver == '6':
            result = (val_mon1 * dol_balb)
        else:
            print("Valor invalido")

    elif type_moneda == '4':
        print("¿---A qué moneda desea convertir?---")
        print("1. Dolar Beliceño - Belice")
        print("2. Colon costarricence - Costa Rica")
        print("3. Dolar Estadounidense - Estados Unidos")
        print("4. Lempira - Honduras")
        print("5. Cordoba - Nicaragua")
        print("6. Balboa - panama") 
        type_conver = (input(''))

        if type_conver == '1':
            result = (val_mon1 * quet_bel)
        elif type_conver == '2':
            result = (val_mon1 * quet_cost)
        elif type_conver == '3':
            result = (val_mon1 * quet_dol)
        elif type_conver == '4':
            result = (val_mon1 * quet_lemp)
        elif type_conver == '5':
            result = (val_mon1 * quet_cord)
        elif type_conver == '6':
            result = (val_mon1 * quet_balb)
        else:
            print("Valor invalido") 
        
    elif type_moneda == '5':
        print("¿---A qué moneda desea convertir?---")
        print("1. Dolar Beliceño - Belice")
        print("2. Colon costarricence - Costa Rica")
        print("3. Dolar Estadounidense - Estados Unidos")
        print("4. Quétzal - Guatemala")
        print("5. Cordoba - Nicaragua")
        print("6. Balboa - panama") 
        type_conver = (input(''))

        if type_conver == '1':
            result = (val_mon1 * lemp_bel)
        elif type_conver == '2':
            result = (val_mon1 * lemp_cost)
        elif type_conver == '3':
            result = (val_mon1 * lemp_dol)
        elif type_conver == '4':
            result = (val_mon1 * lemp_quet)
        elif type_conver == '5':
            result = (val_mon1 * lemp_cord)
        elif type_conver == '6':
            result = (val_mon1 * lemp_balb)
        elif type_moneda == '6':
            print("¿---A qué moneda desea convertir?---")
            print("1. Dolar Beliceño - Belice")
            print("2. Colon costarricence - Costa Rica")
            print("3. Dolar Estadounidense - Estados Unidos")
            print("4. Quétzal - Guatemala")
            print("5. Lempira - Honduras")
            print("6. Balboa - panama")  
            type_conver = (int(''))
        else:
            "Valor invalido"
        if type_conver == '1':
            result = (val_mon1 * cord_bel)
        elif type_conver == '2':
            result = (val_mon1 * cord_cost)
        elif type_conver == '3':
            result = (val_mon1 * cord_dol)
        elif type_conver == '4':
            result = (val_mon1 * cord_quet)
        elif type_conver == '5':
            result = (val_mon1 * cord_lemp)
        elif type_conver == '6':
            result = (val_mon1 * cord_balb)
        else:
            "Valor invalido"

elif type_operacion == '2':
    met_kil = (float(0.001))
    met_pulg = (float(39.3701))
    met_pie = (float(3.28084))
    met_mite = (float(0.006621))
    met_mimar = (float(0.0005399))

    kil_met = (float(1000))
    kil_pulg = (float(39370.1))
    kil_pie = (float(3280.84))
    kil_mite = (float(0.62137))
    kil_mimar = (float(0.5399568))

    pulg_met =(float(0.025399))
    pulg_kil =(float(0.000025))
    pulg_pie =(float(0.08333))
    pulg_mite =(float(0.000015))
    pulg_mimar =(float(0.00001371))

    pie_met = (float(0.304794))
    pie_kil = (float(0.000304))
    pie_pulg = (float(12))
    pie_mite = (float(0.000189))
    pie_mimar = (float(0.00016457))

    mite_met = (float(1609.34))
    mite_kil = (float(1.60934))
    mite_pulg = (float(63360))
    mite_pie = (float(5280))
    mite_mimar = (float(0.8689607))

    mimar_met = (float(1852))
    mimar_kil = (float(1.852))
    mimar_pulg = (float(72913.4))
    mimar_pie = (float(6076.12))
    mimar_mite = (float(1.1508))

    print("---Conversor de Longitudes:---")
    print(" ")

    print("---Escribe el tipo de longitud que deseas convertir:---")
    print("1. Metro")
    print("2. Kilómetro")
    print("3. Pulgada")
    print("4. Pie")
    print("5. Milla Terrestre")
    print("6. Milla Maritima")
    type_long1 = (input(''))
    print("Ingrese el valor de la longitud")
    val1 = float(input(''))
    if type_long1 == '1':
        print("---¿A que unidad desea convertir?---")
        print("1. Kilómetro")
        print("2. Pulgada")
        print("3. Pie")
        print("4. Milla Terrestre")
        print("5. Milla Maritima")
        type_long2 = (input(''))
        
        if type_long2 == '1':
            result = (val1 * met_kil)
        elif type_long2 == '2':
            result = (val1 * met_pulg)
        elif type_long2 == '3':
            result = (val1 * met_pie)
        elif type_long2 == '4':
            result = (val1 * met_mite)
        elif type_long2 == '5':
            result = (val1 * met_mimar)
        else:
            "Valor invalido"

    elif type_long1 == '2':
        print("---¿A que unidad desea convertir?---")
        print("1. Metro")
        print("2. Pulgada")
        print("3. Pie")
        print("4. Milla Terrestre")
        print("5. Milla Maritima")
        type_long2 = (input(''))
        
        if type_long2 == '1':
            result = (val1 * kil_met)
        elif type_long2 == '2':
            result = (val1 * kil_pulg)
        elif type_long2 == '3':
            result = (val1 * kil_pie)
        elif type_long2 == '4':
            result = (val1 * kil_mite)
        elif type_long2 == '5':
            result = (val1 * kil_mimar)
        else:
            "Valor invalido"

    elif type_long1 == '3':
        print("---¿A que unidad desea convertir?---")
        print("1. Metro")
        print("2. Kilómetro")
        print("3. Pie")
        print("4. Milla Terrestre")
        print("5. Milla Maritima")
        type_long2 = (input(''))

        if type_long2 == '1':
            result = (val1 * pulg_met)
        elif type_long2 == '2':
            result = (val1 * pulg_kil)
        elif type_long2 == '3':
            result = (val1 * pulg_pie)
        elif type_long2 == '4':
            result = (val1 * pulg_mite)
        elif type_long2 == '5':
            result = (val1 * pulg_mimar)
        else:
            "Valor invalido"

    elif type_long1 == '4':
        print("---¿A que unidad desea convertir?---")
        print("1. Metro")
        print("2. Kilómetro")
        print("3. Pulgada")
        print("4. Milla Terrestre")
        print("5. Milla Maritima")
        type_long2 = (input(''))

        if type_long2 == '1':
            result = (val1 * pie_met)
        elif type_long2 == '2':
            result = (val1 * pie_kil)
        elif type_long2 == '3':
            result = (val1 * pie_pulg)
        elif type_long2 == '4':
            result = (val1 * pie_mite)
        elif type_long2 == '5':
            result = (val1 * pie_mimar)
        else:
            "Valor invalido"

    elif type_long1 == '5':
        print("---¿A que unidad desea convertir?---")
        print("1. Metro")
        print("2. Kilómetro")
        print("3. Pulgada")
        print("4. Pie")
        print("5. Milla Maritima")
        type_long2 = (input('')) 

        if type_long2 == '6':
            result = (val1 * mite_met)
        elif type_long2 == '2':
            result = (val1 * mite_kil)
        elif type_long2 == '3':
            result = (val1 * mite_pulg)
        elif type_long2 == '4':
            result = (val1 * mite_pie)
        elif type_long2 == '5':
            result = (val1 * mite_mimar)
        else:
            "Valor invalido"

    elif type_long1 == '6':
        print("---¿A que unidad desea convertir?---")
        print("1. Metro")
        print("2. Kilómetro")
        print("3. Pulgada")
        print("4. Pie")
        print("5. Milla Terrestre")
        type_long2 = (input(''))
    
        if type_long2 == '1':
            result = (mimar_met)
        elif type_long2 == '2':
            result = (mimar_kil)
        elif type_long2 == '3':
            result = (mimar_pulg)
        elif type_long2 == '4':
            result = (mimar_pie)
        elif type_long2 == '5':
            result = (mimar_mite)
        else:
            "Valor invalido"
    else:
        "Valor invalido"

elif type_operacion == '3':
    mg_cg = float(0.1)
    mg_g = float(0.001)
    mg_kg = float(0.000001)
    mg_q = float(0.00000001)
    mg_t = float(0.000000001)
    mg_onz = float(0.000035274)
    mg_lib = float(0.00000220462)

    cg_mg = float(10)
    cg_g = float(0.01)
    cg_kg = float(0.00001)
    cg_q = float(0.00001)
    cg_t = float(0.00000001)
    cg_onz = float(0.00035274)
    cg_lib = float(0.000220462)

    g_mg = float(1000)
    g_cg = float(100)
    g_kg = float(0.001)
    g_q = float(100000)
    g_t = float(0.000001)
    g_onz = float(0.035274)
    g_lib = float(0.00220462)

    kg_mg = float(1000000)
    kg_cg  = float(100000)
    kg_g  = float(1000)
    kg_q  = float(0.01)
    kg_t  = float(0.001)
    kg_onz  = float(35.274)
    kg_lib = float(2.20462)

    q_mg = float(100000000)
    q_cg = float(10000000)
    q_g = float(100000)
    q_kg = float(100)
    q_t = float(0.1)
    q_onz = float(3527.396211)
    q_lib = float(220.4622622)

    t_mg = float(1000000000)
    t_cg = float(100000000)
    t_g = float(1000000)
    t_kg = float(1000)
    t_q = float(10)
    t_onz = float(35273.46211)
    t_lib = float(2204.622622)

    onz_mg = float(28349.523)
    onz_cg = float(2834.9523)
    onz_g = float(28.349523)
    onz_kg = float(0.028349523)
    onz_q = float(0.00028349523)
    onz_t = float(0.000028349499999999997)
    onz_lib = float(0.0625)

    lib_mg = float(453692.37)
    lib_cg = float(45369.237)
    lib_g = float(453.69237)
    lib_kg = float(0.45369237)
    lib_q = float(0.004535924)
    lib_t = float(0.000453592)
    lib_onz = float(16)



    print("---Conversor de Masa---")
    print("---Elije la unidad a convertir---")
    print("1. Miligramo")
    print("2. Centigramo")
    print("3. Gramo")
    print("4. Kilogramo")
    print("5. Quintal")
    print("6. Tonelada")
    print("7. Onza")
    print("8. Libra")
    type_masa = (input(''))
    print("Ingrese el valor de la masa a convertir:")
    val = float(input(''))

    if type_masa == '1':
        print("---¿A que unidad desea convertir?---")
        print("1. Centigramo")
        print("2. Gramo")
        print("3. Kilogramo")
        print("4. Quintal")
        print("5. Tonelada")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * mg_cg)
        elif type_masa2 == '3':
            result = (val * mg_g)
        elif type_masa2 == '4':
            result = (val * mg_kg)
        elif type_masa2 == '5':
            result = (val * mg_q)
        elif type_masa2 == '6':
            result = (val * mg_t)
        elif type_masa2 == '7':
            result = (val * mg_onz)
        elif type_masa2 == '8':
            result = (val * mg_lib)
        else:
            print("Valor invalido")
    elif type_masa == '2':
        print("---¿A que unidad desea convertir?---")
        print("1. Miligramo")
        print("2. Gramo")
        print("3. Kilogramo")
        print("4. Quintal")
        print("5. Tonelada")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * cg_mg)
        elif type_masa2 =='2':
            result = (val * cg_g)
        elif type_masa2 =='3':
            result = (val * cg_kg)
        elif type_masa2 =='4':
            result = (val * cg_q)
        elif type_masa2 =='5':
            result = (val * cg_t)
        elif type_masa2 =='6':
            result = (val * cg_onz)
        elif type_masa2 =='7':
            result = (val * cg_lib)
        else:
            print("Valor invalido")
    elif type_masa == '3':
        print("---¿A que unidad desea convertir?---")
        print("1. Miligramo")
        print("2. centigramo")
        print("3. Kilogramo")
        print("4. Quintal")
        print("5. Tonelada")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * g_mg)
        elif type_masa2 =='2':
            result = (val * g_cg)
        elif type_masa2 =='3':
            result = (val * g_kg)
        elif type_masa2 =='4':
            result = (val * g_q)
        elif type_masa2 =='5':
            result = (val * g_t)
        elif type_masa2 =='6':
            result = (val * g_onz)
        elif type_masa2 =='7':
            result = (val * g_lib)
        else:
            print("Valor invalido")
    elif type_masa == '4':
        print = ("¿A que valor de unidad desea convertir?")
        print("1. Miligramo")
        print("2. Centigramo")
        print("3. Gramo")
        print("4. Quintal")
        print("5. Tonelada")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * kg_mg)
        elif type_masa2 == '2':
            result = (val * kg_cg)
        elif type_masa2 == '3':
            result = (val * kg_g)
        elif type_masa2 == '4':
            result = (val * kg_q)
        elif type_masa2 == '5':
            result = (val * kg_t)
        elif type_masa2 == '6':
            result = (val * kg_onz)
        elif type_masa2 == '7':
            reuslt = (val * kg_lib)
        else:
            print("Valor invalido")
    elif type_masa == '5':
        print("¿A que valor de unidad desea convertir?")
        print("1. Miligramo")
        print("2. Centigramo")
        print("3. Gramo")
        print("4. Kilogramo")
        print("5. Tonelada")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))
        if type_masa2 == '1':
            result = (val * q_mg)
        elif type_masa2 == '2':
            result = (val * q_cg)
        elif type_masa2 == '3':
            result = (val * q_g)
        elif type_masa2 == '4':
            result = (val * q_kg)
        elif type_masa2 == '5':
            result = (val * q_t)
        elif type_masa2 == '6':
            result = (val * q_onz)
        elif type_masa2 == '7':
            result = (val * q_lib)
    elif type_masa == '6':
        print("¿A que valor de unidad desea convertir?")
        print("1. Miligramo")
        print("2. Centigramo")
        print("3. Gramo")
        print("4. Kilogramo")
        print("5. Quintal")
        print("6. Onza")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * onz_mg)
        elif type_masa2 == '2':
            result = (val * onz_mg)
        elif type_masa2 == '3':
            result = (val * onz_mg)
        elif type_masa2 == '4':
            result = (val * onz_mg)
        elif type_masa2 == '5':
            result = (val * onz_mg)
        elif type_masa2 == '6':
            result = (val * onz_mg)
        elif type_masa2 == '7':
            result = (val * onz_mg)
        else:
            print("Valor invalido")
    elif type_masa == '7':
        print("¿A que valor de unidad desea convertir?")
        print("1. Miligramo")
        print("2. Centigramo")
        print("3. Gramo")
        print("4. Kilogramo")
        print("5. Quintal")
        print("6. Tonelada")
        print("7. Libra")
        type_masa2 = (input(''))

        if type_masa2 == '1':
            result = (val * onz_mg)
        elif type_masa2 == '2':
            result = (val * onz_cg)
        elif type_masa2 == '3':
            result = (val * onz_g)
        elif type_masa2 == '4':
            result = (val * onz_kg)
        elif type_masa2 == '5':
            result = (val * onz_q)
        elif type_masa2 == '6':
            result = (val * onz_t)
        elif type_masa2 == '7':
            result = (val * onz_lib)
        else:
            print("Valor invalido")
    elif type_masa == '8':
        print("¿A que valor de unidad desea convertir?")
        print("1. Miligramo")
        print("2. Centigramo")
        print("3. Gramo")
        print("4. Kilogramo")
        print("5. Quintal")
        print("6. Tonelada")
        print("7. Onza")
        type_masa2 = (input(''))
        if type_masa2 == '1':
            result = (val * lib_mg)
        elif type_masa2 == '2':
            result = (val * lib_cg)
        elif type_masa2 == '3':
            result = (val * lib_g)
        elif type_masa2 == '4':
            result = (val * lib_kg)
        elif type_masa2 == '5':
            result = (val * lib_q)
        elif type_masa2 == '6':
            result = (val * lib_t)
        elif type_masa2 == '7':
            result = (val * lib_onz)  
        else:
            print("Valor invalido") 
elif type_operacion == '4':
    bit_byt=(0.125)
    bit_kb=(0.0001220703125)
    bit_mb=(0.0000001192092895507813)
    bit_gb=(0.00000000011641532182693486328125)
    bit_tb=(0.000000000000113686837721616077423095703125)

    byt_bit=(8)
    byt_kb=(0.0078125)
    byt_mb=(0.00000762939453125)
    byt_gb=(0.000000007450580596923828125)
    byt_tb=(0.0000000000072759576141834259033203125)

    kb_bit=(8192)
    kb_byt=(1024)
    kb_mb=(0.0009765625)
    kb_gb=(0.00000095367431640625)
    kb_tb=(0.000000000931322574615478515625)

    mb_bit=(8388608)
    mb_byt=(1048576)
    mb_kb=(1024)
    mb_gb=(0.0009765625)
    mb_tb=(0.00000095367431640625)

    gb_bit=(8589934592)
    gb_byt=(1073741824)
    gb_kb=(1048576)
    gb_mb=(1024)
    gb_tb=(0.0009765625)

    tb_bit=(8796093022208)
    tb_byt=(1099511627776)
    tb_kb=(1073741824)
    tb_mb=(1048576)
    tb_gb=(1024)

    
    print("---Conversor de Almacenamiento:---")
    print("---¿Que unidad de almacenamiento desea convertir?---")
    print("1. Bit")
    print("2. Byte")
    print("3. Kilobyte")
    print("4. Megabyte")
    print("5. Gigabyte")
    print("6. Terabyte")
    type_bit = (input(''))
    print("---Escribe el valor de la unidad a convertir---")
    val = (float(input("")))
    if type_bit == '1':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Byte")
        print("2. Kilobyte")
        print("3. Megabyte")
        print("4. Gigabyte")
        print("5. Terabyte")
        type_bit2 = (input(''))
        if type_bit2 == '1':
            result = (val * bit_byt)
        elif type_bit2 == '2':
            result = (val * bit_kb)
        elif type_bit2 == '3':
            result = (val * bit_mb)
        elif type_bit2 == '4':
            result = (val * bit_gb)
        elif type_bit2 == '5':
            result = (val * bit_tb)
        else:
            print("Valor invalido")
    elif type_bit == '2':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Bit")
        print("2. Kilobyte")
        print("3. Megabyte")
        print("4. Gigabyte")
        print("5. Terabyte")
        type_bit2 = (input(''))
        print("---Escribe el valor de la unidad a convertir---")
        val = (float(input("")))
        if type_bit2 == '1':
            result = (val * byt_bit)
        elif type_bit2 == '2':
            result = (val * byt_kb)
        elif type_bit2 == '3':
            result = (val * byt_mb)
        elif type_bit2 == '4':
            result = (val * byt_gb)
        elif type_bit2 == '5':
            result = (val * byt_tb)
        else:
            print("Valor invalido")
     
    elif type_bit == '3':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Bit")
        print("2. Byte")
        print("3. Megabyte")
        print("4. Gigabyte")
        print("5. Terabyte")
        type_bit2 = (input(''))
        print("---Escribe el valor de la unidad a convertir---")
        val = (float(input("")))
        if type_bit2 == '1':
            result = (val * kb_bit)
        elif type_bit2 == '2':
            result = (val * kb_byt)
        elif type_bit2 == '3':
            result = (val * kb_mb)
        elif type_bit2 == '4':
            result = (val * kb_gb)
        elif type_bit2 == '5':
            result = (val * kb_tb)
        else:
            print("Valor invalido")

    elif type_bit == '4':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Bit")
        print("2. Byte")
        print("3. Kilobyte")
        print("4. Gigabyte")
        print("5. Terabyte")
        type_bit2 = (input(''))
        print("---Escribe el valor de la unidad a convertir---")
        val = (float(input("")))
        if type_bit2 == '1':
            result = (val * mb_bit)
        elif type_bit2 == '2':
            result = (val * mb_byt)
        elif type_bit2 == '3':
            result = (val * mb_kb)
        elif type_bit2 == '4':
            result = (val * mb_gb)
        elif type_bit2 == '5':
            result = (val * mb_tb)
        else:
            print("Valor invalido")
    elif type_bit == '5':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Bit")
        print("2. Byte")
        print("3. Kilobyte")
        print("4. Megabyte")
        print("5. Terabyte")
        type_bit2 = (input(''))
        print("---Escribe el valor de la unidad a convertir---")
        val = (float(input("")))
        if type_bit2 == '1':
            result = (val * gb_bit)
        elif type_bit2 == '2':
            result = (val * gb_byt)
        elif type_bit2 == '3':
            result = (val * gb_kb)
        elif type_bit2 == '4':
            result = (val * gb_mb)
        elif type_bit2 == '5':
            result = (val * gb_tb)
        else:
            print("Valor invalido")

         
    elif type_bit == '6':
        print("---¿A que unidad de almacenamiento desea convertir?---")
        print("1. Bit")
        print("2. Byte")
        print("3. Kilobyte")
        print("4. Megabyte")
        print("5. Gigabyte")
        type_bit2 = (input(''))
        print("---Escribe el valor de la unidad a convertir---")
        val = (float(input("")))

        if type_bit2 == '1':
            result = (val * tb_bit)
        elif type_bit2 == '2':
            result = (val * tb_byt)
        elif type_bit2 == '3':
            result = (val * tb_kb)
        elif type_bit2 == '4':
            result = (val * tb_mb)
        elif type_bit2 == '5':
            result = (val * tb_gb)
        else:
            print("Valor invalido")
    else:
        print("Valor invalido")
elif type_operacion == '5':
    seg_min = float(0.01666666666666666666666666666667)
    seg_hora =float(0.00027777777777777777777777777777778)
    seg_dia = float(0.000011574074074074074074074074074074)
    seg_sem =float(0.0000016534391534391534391534391534392)
    seg_años =float(0.000000031709791983764586504312531709792)

    min_seg =float(60)
    min_hora =float(0.01666666666666666666666666666667)
    min_dia =float(0.00069444444444444444444444444444444)
    min_sem =float(0.00099206349206349206349206349206349)
    min_años = float(0.00000031685678073510773130544993662864)

    hora_seg =float(3600)
    hora_min =float(60)
    hora_dia =float(0.04166666666666666666666666666667)
    hora_sem =float(0.000099206349206349206349206349206349)
    hora_años =float(0.0000019025875190258751902587519025875)

    dia_seg =float(86400)
    dia_min =float(1440)
    dia_hora =float(24)
    dia_sem= float(0.14285714285714285714285714285714)
    dia_años=float(0.00273972602739726027397260273973)

    sem_seg=float(604800)
    sem_min=float(10080)
    sem_hora=float(168)
    sem_dias=float(7)
    sem_años=float(0.01917808219178082191780821917808)

    años_seg=float(31536000)
    años_min=float(525600)
    años_hora=float(5760)
    años_dias=float(365)
    años_sem=float(52.142857142857142857142857142857)

    print("---Conversor de Tiempo:---")
    print("1. Segundos")
    print("2. Minutos")
    print("3. Horas")
    print("4. Dias")
    print("5. Semanas")
    print("6. Años")
    type = (input(''))
    print("---Ingrese la cantidad de tiempo:---")
    val = (float(input('')))

    if type == '1':
        print("---A que valor desea convertir:---")
        print("1. Minutos")
        print("2. Horas")
        print("3. Dias")
        print("4. Semanas")
        print("5. Años")
        type2 = (input(''))
        if type2 == '1':
            result = (val * seg_min)
        elif type2 == '2':
            result = (val * seg_hora)
        elif type2 == '3':
            result = (val * seg_dia)
        elif type2 == '4':
            result = (val * seg_sem)
        elif type2 == '5':
            result = (val * seg_años)
        else:
            print("Valor invalido")
    elif type == '2':
        print("---A que valor desea convertir:---")
        print("1. Segundos")
        print("2. Horas")
        print("3. Dias")
        print("4. Semanas")
        print("5. Años")
        type2 = (input(''))
        if type2 == '1':
            result = (val * min_seg)
        elif type2 =='2':
            result = (val * min_hora)
        elif type2 =='2':
            result = (val * min_dia)
        elif type2 =='2':
            result = (val * min_sem)
        elif type2 =='2':
            result = (val * min_años)
        else:
            print("Valor invalido")
    elif type == '3':
        print("---A que valor desea convertir:---")
        print("1. Segundos")
        print("2. Minutos")
        print("4. Dias")
        print("5. Semanas")
        print("6. Años")
        type2 = (input(''))
        if type2 == '1':
            result = (val * hora_seg)
        elif type2 == '2':
            result = (val * hora_min)
        elif type2 == '3':
            result = (val * hora_dia)
        elif type2 == '4':
            result = (val * hora_sem)
        elif type2 == '5':
            result = (val * hora_años)
        else:
            print("Valor invalido")
    elif type == '4':
        print("---A que valor desea convertir:---")
        print("1. Segundos")
        print("2. Minutos")
        print("3. Horas")
        print("4. Semanas")
        print("5. Años")
        type2 = (input(''))
        if type2 == '1':
            result = (val * dia_seg)
        elif type2 == '2':
            result = (val * dia_min)
        elif type2 == '3':
            result = (val * dia_hora)
        elif type2 == '4':
            result = (val * dia_sem)
        elif type2 == '5':
            result = (val * dia_años)
        else:
            print("Valor invalido")
    elif type == '5':
        print("---A que valor desea convertir:---")
        print("1. Segundos")
        print("2. Minutos")
        print("3. Horas")
        print("4. Dias")
        print("5. Años")
        type2 = (input(''))
        if type2 == '1':
            result = (val * sem_seg)
        elif type2 == '2':
            result = (val * sem_min)
        elif type2 == '3':
            result = (val * sem_hora)
        elif type2 == '4':
            result = (val * sem_dias)
        elif type2 == '5':
            result = (val * sem_años)
        else:
            print("Valor invalido")
    elif type == '6':
        print("---A que valor desea convertir:---")
        print("1. Segundos")
        print("2. Minutos")
        print("3. Horas")
        print("4. Dias")
        print("5. Semanas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * años_seg)
        elif type2 == '2':
            result = (val * años_min)
        elif type2 == '3':
            result = (val * años_hora)
        elif type2 == '4':
            result = (val * años_dias)
        elif type2 == '5':
            result = (val * años_sem)
        else:
            print("Valor invalido")
    else:
        print("Valor invalido")
elif type_operacion == '6':
    dm_cm = float(10)
    dm_m = float(0.1)
    dm_pulg = float(3.937)
    dm_km = float(0.0001)
    dm_pie = float(0.328)
    dm_gal = float(0.0264172)
    dm_l = float(1)

    cm_dm = float(0.1)
    cm_m = float(0.01)
    cm_pulg = float(0.3937)
    cm_km = float(0.00001)
    cm_pie = float(0.0328)
    cm_gal = float(0.00264172)
    cm_l = float(0.01)

    m_dm = float(10)
    m_cm = float(100)
    m_pulg = float(39.37)
    m_km = float(0.001)
    m_pie = float(3.281)
    m_gal = float(264.172)
    m_l = float(1000)

    pulg_dm = float(0.254)
    pulg_cm = float(2.54)
    pulg_m = float(0.0254)
    pulg_km = float(0.0000254)
    pulg_pie = float(0.0833)
    pulg_gal = float(0.004329)
    pulg_l = float(0.0163871)

    km_dm = float(10000)
    km_cm = float(100000)
    km_m = float(1000)
    km_pulg = float(39370.1)
    km_pie = float(3280.84)
    km_gal = float(2641.72)
    km_l = float(1000000)

    pie_dm = float(3.048)
    pie_cm = float(30.48)
    pie_m = float(0.3048)
    pie_pulg = float(12)
    pie_km = float(0.0003048)
    pie_gal = float(8)
    pie_l = float(28.3168)

    gal_dm = float(37.8541)
    gal_cm = float(3785.41)
    gal_m = float(0.00378541)
    gal_pulg = float(231)
    gal_km = float(0.00000378541)
    gal_pie = float(0.125)
    gal_l = float(3.78541)

    l_dm = float(1)
    l_cm = float(100)
    l_m = float(0.001)
    l_pulg = float(61.0237)
    l_km = float(0.000001)
    l_pie = float(0.03281)
    l_gal = float(0.264172)
    print("---Conversor de Volumen:---")
    print("---¿Qué valor desea convertir?---")
    print("1. Decimetro^3")
    print("2. Centimetro^3")
    print("3. Metro^3")
    print("4. Kilometro^3")
    print("5. Pulgadas^3")
    print("6. Pie^3")
    print("7. Galones^3")
    print("8. Litros^3")
    type1 = (input(''))
    print("---Escribe el valor de la unidad a convertir---")
    val =(float(input('')))
    if type1 == '1':
        print("---A que valor desea convertir---")
        print("1. Centimetro^3")
        print("2. Metro^3")
        print("3. Kilometro^3")
        print("4. Pulgadas^3")
        print("5. Pie^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * dm_cm)
        elif type2 == '2':
            result =(val * dm_m)
        elif type2 == '3':
            result =(val * dm_km)
        elif type2 == '4':
            result =(val * dm_pulg)
        elif type2 == '5':
            result =(val * dm_pie)
        elif type2 == '6':
            result =(val * dm_gal)
        elif type2 == '7':
            result =(val * dm_l)
        else:
            print("Valor invalido")
    elif type1 == '2':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Metro^3")
        print("3. Kilometro^3")
        print("4. Pulgadas^3")
        print("5. Pie^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * cm_dm)
        elif type2 == '2':
            result =(val * cm_m)
        elif type2 == '3':
            result =(val * cm_km)
        elif type2 == '4':
            result =(val * cm_pulg)
        elif type2 == '5':
            result =(val * cm_pie)
        elif type2 == '6':
            result =(val * cm_gal)
        elif type2 == '7':
            result =(val * cm_l)
        else:
            print("Valor invalido")
    elif type1 == '3':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Kilometro^3")
        print("4. Pulgadas^3")
        print("5. Pie^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * m_dm)
        elif type2 == '2':
            result =(val * m_cm)
        elif type2 == '3':
            result =(val * m_km)
        elif type2 == '4':
            result =(val * m_pulg)
        elif type2 == '5':
            result =(val * m_pie)
        elif type2 == '6':
            result =(val * m_gal)
        elif type2 == '7':
            result =(val * m_l)
        else:
            print("Valor invalido")
    elif type1 == '4':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Metro^3")
        print("4. Pulgadas^3")
        print("5. Pie^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * km_dm)
        elif type2 == '2':
            result =(val * km_cm)
        elif type2 == '3':
            result =(val * km_m)
        elif type2 == '4':
            result =(val * km_pulg)
        elif type2 == '5':
            result =(val * km_pie)
        elif type2 == '6':
            result =(val * km_gal)
        elif type2 == '7':
            result =(val * km_l)
        else:
            print("Valor invalido")
    elif type1 == '5':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Metro^3")
        print("4. Kilometro^3")
        print("5. Pie^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * pulg_dm)
        elif type2 == '2':
            result =(val * pulg_cm)
        elif type2 == '3':
            result =(val * pulg_m)
        elif type2 == '4':
            result =(val * pulg_km)
        elif type2 == '5':
            result =(val * pulg_pie)
        elif type2 == '6':
            result =(val * pulg_gal)
        elif type2 == '7':
            result =(val * pulg_l)
        else:
            print("Valor invalido")
    elif type1 == '6':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Metro^3")
        print("4. Kilometro^3")
        print("5. Pulgadas^3")
        print("6. Galones^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * pie_dm)
        elif type2 == '2':
            result =(val * pie_cm)
        elif type2 == '3':
            result =(val * pie_m)
        elif type2 == '4':
            result =(val * pie_km)
        elif type2 == '5':
            result =(val * pie_pulg)
        elif type2 == '6':
            result =(val * pie_gal)
        elif type2 == '7':
            result =(val * pie_l)
        else:
            print("Valor invalido")
    elif type1 == '7':       
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Metro^3")
        print("4. Kilometro^3")
        print("5. Pulgadas^3")
        print("6. Pie^3")
        print("7. Litros^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * gal_dm)
        elif type2 == '2':
            result =(val * gal_cm)
        elif type2 == '3':
            result =(val * gal_m)
        elif type2 == '4':
            result =(val * gal_km)
        elif type2 == '5':
            result =(val * gal_pulg)
        elif type2 == '6':
            result =(val * gal_pie)
        elif type2 == '7':
            result =(val * gal_l)
        else:
            print("Valor invalido")
    elif type1 == '8':
        print("---A que valor desea convertir---")
        print("1. Decimetro^3")
        print("2. Centimetro^3")
        print("3. Metro^3")
        print("4. Kilometro^3")
        print("5. Pulgadas^3")
        print("6. Pie^3")
        print("7. Galones^3")
        type2 = (input(''))
        if type2 == '1':
            result =(val * l_dm)
        elif type2 == '2':
            result =(val * l_cm)
        elif type2 == '3':
            result =(val * l_m)
        elif type2 == '4':
            result =(val * l_km)
        elif type2 == '5':
            result =(val * l_pulg)
        elif type2 == '6':
            result =(val * l_pie)
        elif type2 == '7':
            result =(val * l_gal)
        else:
            print("Valor invalido")
    else:
        print("Valor invalido")
elif type_operacion == '7':
    print("---Conversor de Area:---")
    m_cm = float(10000)
    m_dm = float(100)
    m_km = float(0.000001)
    m_pulg = float(1550.0031)
    m_pies = float(10.7639)
    m_hec = float(0.0001)
    m_acr = float(0.000247105)
    m_mill = float(0.000000386102)

    cm_m = float(0.0001)
    cm_dm = float(0.01)
    cm_km = float(0.0000000001)
    cm_pulg = float(0.155)
    cm_pies = float(0.001076)
    cm_hec = float(0.00000001)
    cm_acr = float(0.0000000247105)
    cm_mill = float(0.0000000000386102)

    dm_m = float(0.01)
    dm_cm = float(100)
    dm_km = float(0.00000001)
    dm_pulg = float(15.5)
    dm_pies = float(0.107639)
    dm_hec = float(0.000001)
    dm_acr = float(0.00000247105)
    dm_mill = float(0.00000000386102)

    km_m = float(1000000)
    km_cm = float(100000000000)
    km_dm = float(100000000)
    km_pulg = float(1550003100)
    km_pies = float(10763910.4)
    km_hec = float(10000)
    km_acr = float(247.105)
    km_mill = float(0.386102)

    pulg_m = float(0.00064516)
    pulg_cm = float(6.4516)
    pulg_dm = float(0.064516)
    pulg_km = float(0.00000000064516)
    pulg_pies = float(0.00694444)
    pulg_hec = float(0.000000064516)
    pulg_acr = float(0.0000001594225)
    pulg_mill = float(0.0000000002490975)

    pies_m = float(0.092903)
    pies_cm = float(929.03)
    pies_dm = float(9.2903)
    pies_km = float(0.000000092903)
    pies_pulg = float(144)
    pies_hec = float(0.0000092903)
    pies_acr = float(0.0000229568)
    pies_mill = float(0.0000000358701)

    hec_m = float(10000)
    hec_cm = float(100000000000)
    hec_dm = float(100000000)
    hec_km = float(0.01)
    hec_pulg = float(15500031)
    hec_pies = float(107639.104)
    hec_acr = float(2.47105)
    hec_mill = float(0.00386102)

    acr_m = float(4046.86)
    acr_cm = float(40468600)
    acr_dm = float(404686)
    acr_km = float(0.00404686)
    acr_pulg = float(6272640)
    acr_pies = float(43560)
    acr_hec = float(0.404686)
    acr_mill = float(0.0015625)

    mill_m = float(2589988.11)
    mill_cm = float(2589988110336)
    mill_dm = float(25899881103.36)
    mill_km = float(2.589988)
    mill_pulg = float(4014489600)
    mill_pies = float(27878400)
    mill_hec = float(258.998811)
    mill_acr = float(640)
    print("---Ingrese que unidad desea convertir---")
    print("1. Metros cuadrados")
    print("2. Centimetros cuadrados")
    print("3. Decimetros cuadrados")
    print("4. Kilometros cuadrados")
    print("5. Pulgadas cuadradas")
    print("6. Pies cuadrados")
    print("7. Hectareas")
    print("8. Acres")
    print("9. Millas cuadradas")
    type1 = (input(''))
    print("---Ingrese el valor de la unidad a convertir---")
    val = (float(input('')))
    if type1 == '1':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Centimetros cuadrados")
        print("2. Decimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * m_cm)
        elif type2 == '2':
            result = (val * m_dm)
        elif type2 == '3':
            result = (val * m_km)
        elif type2 == '4':
            result = (val * m_pulg)
        elif type2 == '5':
            result = (val * m_pies)
        elif type2 == '6':
            result = (val * m_hec)
        elif type2 == '7':
            result = (val * m_acr)
        elif type2 == '8':
            result = (val * m_mill)
        else:
            print("Valor invalido")
    elif type1 == '2':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Decimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * cm_m)
        elif type2 == '2':
            result = (val * cm_dm)
        elif type2 == '3':
            result = (val * cm_km)
        elif type2 == '4':
            result = (val * cm_pulg)
        elif type2 == '5':
            result = (val * cm_pies)
        elif type2 == '6':
            result = (val * cm_hec)
        elif type2 == '7':
            result = (val * cm_acr)
        elif type2 == '8':
            result = (val * cm_mill)
        else:
            print("Valor invalido")
    elif type1 == '3':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * dm_m)
        elif type2 == '2':
            result = (val * dm_cm)
        elif type2 == '3':
            result = (val * dm_km)
        elif type2 == '4':
            result = (val * dm_pulg)
        elif type2 == '5':
            result = (val * dm_pies)
        elif type2 == '6':
            result = (val * dm_hec)
        elif type2 == '7':
            result = (val * dm_acr)
        elif type2 == '8':
            result = (val * dm_mill)
        else:
            print("Valor invalido")
    elif type1 == '4':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * km_m)
        elif type2 == '2':
            result = (val * km_cm)
        elif type2 == '3':
            result = (val * km_dm)
        elif type2 == '4':
            result = (val * km_pulg)
        elif type2 == '5':
            result = (val * km_pies)
        elif type2 == '6':
            result = (val * km_hec)
        elif type2 == '7':
            result = (val * km_acr)
        elif type2 == '8':
            result = (val * km_mill)
        else:
            print("Valor invalido")
    elif type1 == '5':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * pulg_m)
        elif type2 == '2':
            result = (val * pulg_cm)
        elif type2 == '3':
            result = (val * pulg_dm)
        elif type2 == '4':
            result = (val * pulg_km)
        elif type2 == '5':
            result = (val * pulg_pies)
        elif type2 == '6':
            result = (val * pulg_hec)
        elif type2 == '7':
            result = (val * pulg_acr)
        elif type2 == '8':
            result = (val * pulg_mill)
        else:
            print("Valor invalido")
    elif type1 == '6':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * pies_m)
        elif type2 == '2':
            result = (val * pies_cm)
        elif type2 == '3':
            result = (val * pies_dm)
        elif type2 == '4':
            result = (val * pies_km)
        elif type2 == '5':
            result = (val * pies_pulg)
        elif type2 == '6':
            result = (val * pies_hec)
        elif type2 == '7':
            result = (val * pies_acr)
        elif type2 == '8':
            result = (val * pies_mill)
        else:
            print("Valor invalido")
    elif type1 == '7':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * hec_m)
        elif type2 == '2':
            result = (val * hec_cm)
        elif type2 == '3':
            result = (val * hec_dm)
        elif type2 == '4':
            result = (val * hec_km)
        elif type2 == '5':
            result = (val * hec_pulg)
        elif type2 == '6':
            result = (val * hec_pies)
        elif type2 == '7':
            result = (val * hec_acr)
        elif type2 == '8':
            result = (val * hec_mill)
        else:
            print("Valor invalido")
    elif type1 == '8':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Hectareas")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * acr_m)
        elif type2 == '2':
            result = (val * acr_cm)
        elif type2 == '3':
            result = (val * acr_dm)
        elif type2 == '4':
            result = (val * acr_km)
        elif type2 == '5':
            result = (val * acr_pulg)
        elif type2 == '6':
            result = (val * acr_pies)
        elif type2 == '7':
            result = (val * acr_hec)
        elif type2 == '8':
            result = (val * acr_mill)
        else:
            print("Valor invalido")
    elif type1 == '9':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Hectareas")
        print("8. Acres")
        type2 = (input(''))
        if type2 == '1':
            result = (val * mill_m)
        elif type2 == '2':
            result = (val * mill_cm)
        elif type2 == '3':
            result = (val * mill_dm)
        elif type2 == '4':
            result = (val * mill_km)
        elif type2 == '5':
            result = (val * mill_pulg)
        elif type2 == '6':
            result = (val * mill_pies)
        elif type2 == '7':
            result = (val * mill_hec)
        elif type2 == '8':
            result = (val * mill_acr)
        else:
            print("Valor invalido")
    else: 
        print("Valor invalido")
elif type_operacion == '8':
    man_m = float(6987)
    man_hec = float(0.6987)
    man_acr = float(1.7259)
    man_km = float(0.00006987)
    man_pies = float(75003.89)
    man_pulg = float(10890078.24)
    man_mill = float(0.00002707)

    print("---Convertir Manzanas:---")
    print("---Ingrese la cantidad de manzanas---")
    val = (float(input('')))
    print("---¿A que unidad desea convertir las manzanas---")
    print("1. Metros Cuadrados")
    print("2. Hectáreas")
    print("3. Acres")
    print("4. Kilometros cuadrados")
    print("5. Pies cuadrados")
    print("6. Pulgadas cuadradas")
    print("7. Millas cuadradas")
    type1 = (input(''))
    if type1 == '1':
        result = (val * man_m)
    elif type1 == '2':
        result = (val * man_hec)
    elif type1 == '3':
        result = (val * man_acr)
    elif type1 == '4':
        result = (val * man_km)
    elif type1 == '5':
        result = (val * man_pies)
    elif type1 == '6':
        result = (val * man_pulg)
    elif type1 == '7':
        result = (val * man_mill)
    else:
        print("Valor invalido")

elif type_operacion == '9': 
    hec_m = float(10000)
    hec_km = float(0.01)
    hec_acr = float(2.47105)
    hec_mi = float(0.00386102)
    hec_tareas = float(143)
    print("---Conversor de Hectareas:---")
    print("---Ingrese el valor en hectareas---")  
    val = (float(input('')))
    print("---¿A que valor desea convertir?---")
    print("1. Metros cuadrados") 
    print("2. Kilometros cuadrados")
    print("3. Acres")
    print("4. Millas cuadradas")
    print("5. Tareas")
    type1 =(input('')) 
    if type1 == '1':
        result = (val * hec_m)
    elif type1 == '2':
        result = (val * hec_km)
    elif type1 == '3':
        result = (val * hec_acr)
    elif type1 == '4':
        result = (val * hec_mi)
    elif type1 == '5':
        result = (val * hec_tareas)
    else:
        print("Valor invalido")
else:
    print("Operación no válida")

print(result)
