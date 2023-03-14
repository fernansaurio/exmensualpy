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
    print(result)

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
    print("Conversor de Tiempo:")
elif type_operacion == '6':
    print("Conversor de Volumen:")
elif type_operacion == '7':
    print("Conversor de Area:")
elif type_operacion == '8':
    print("Convertir Manzanas:")
elif type_operacion == '9': 
    print("Conversor de Hectareas:")    
else:
    print("Operación no válida")

print(result)
