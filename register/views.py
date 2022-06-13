from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from register.forms import FormUser, FormVeh
from register.models import user, vehicle
from validate_docbr import CPF

#------------------------------------------------------------------------------------

#1.0 Usuário
#1.1 Tela INICIAL da área usuário
def user_list(request):
    users = user.objects.all()
    template_name = 'user_list.html'
    context = {
        'users': users,
    }

    return render(request, template_name, context)

#1.2 Tela de CADASTRO da área usuário
def user_add(request):
    if request.POST:
        form = FormUser(request.POST or None)
        if form.is_valid():
            user_username = request.POST.get('username')
            user_cpf = request.POST.get('cpf')
            user_enrollment = request.POST.get('enrollment')
            user_email = request.POST.get('email')
            user_phone = request.POST.get('phone')

            #Verifica preenchimento dos campos
            if len(user_username.strip()) == 0 or len(user_cpf.strip()) == 0 or len(user_enrollment.strip()) == 0 or len(user_email.strip()) == 0 or len(user_phone.strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('/reg/user_add')
            else:
                #Verifica se o CPF é válido através de uma biblioteca 'pip install validate docbr'
                cpf = CPF()
                if cpf.validate(user_cpf) == False:
                    messages.add_message(request, constants.ERROR, 'CPF não validado')
                    return redirect('/reg/user_add')
                else:
                    # Verifica se os valores já estão cadastrados e, caso não estejam, salva os valores no banco de dados
                    user_filter_cpf = user.objects.filter(cpf = user_cpf)
                    user_filter_enrollment = user.objects.filter(enrollment = user_enrollment)
                    user_filter_email = user.objects.filter(email = user_email)
                    user_filter_phone = user.objects.filter(phone = user_phone)

                    if user_filter_cpf.exists():
                        messages.add_message(request, constants.ERROR, 'CPF já cadastrado')
                        return redirect('/reg/user_add')
                    elif user_filter_enrollment.exists():
                        messages.add_message(request, constants.ERROR, 'Matrícula já cadastrada')
                        return redirect('/reg/user_add')
                    elif user_filter_email.exists():
                        messages.add_message(request, constants.ERROR, 'Email já cadastrado')
                        return redirect('/reg/user_add')
                    elif user_filter_phone.exists():
                        messages.add_message(request, constants.ERROR, 'Telefone já cadastrado')
                        return redirect('/reg/user_add')    
                    else:
                        try:
                            form.save()
                            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado')
                            return redirect('/reg/user_add')
                        except:
                            pass
    else:
        form = FormUser()
                    

    template_name = 'user_add.html'
    context = {
        'form': form
    }
    
    return render(request, template_name, context)

#1.3 Tela de EDIÇÃO da área usuário
def user_edit(request, user_pk):
    user_obj = user.objects.get(pk = user_pk)
    form = FormUser(request.POST or None, instance = user_obj)
    
    if request.POST:
        if form.is_valid():
            user_username = request.POST.get('username')
            user_cpf = request.POST.get('cpf')
            user_enrollment = request.POST.get('enrollment')
            user_email = request.POST.get('email')
            user_phone = request.POST.get('phone')

            #Verifica preenchimento dos campos
            if len(user_username.strip()) == 0 or len(user_cpf.strip()) == 0 or len(user_enrollment.strip()) == 0 or len(user_email.strip()) == 0 or len(user_phone.strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('/reg/user_add')
            else:
                try:
                    form.save()
                    return redirect('/reg/user_edit')
                except:
                    pass

    template_name = 'user_edit.html'
    context = {
        'user_obj': user_obj,
        'form': form
    }

    return render(request, template_name, context)

#1.4 Função remove da área usuário
def user_remove(user_pk):
    user_obj = user.objects.get(pk = user_pk)
    user_obj.delete()

    return redirect('/reg/user')

#------------------------------------------------------------------------------------

#2.0 Automóvel
#2.1 Tela INICIAL da área Automóvel
def veh_list(request):
    vehs = vehicle.objects.all()
    template_name = 'veh_list.html'
    context = {
        'vehs': vehs
    }

    return render(request, template_name, context)

#2.2 Tela de CADASTRO da área Automóvel
def veh_add(request):
    if request.POST:
        form = FormVeh(request.POST or None)
        if form.is_valid():
            veh_brand = request.POST.get('brand')
            veh_model = request.POST.get('model')
            veh_plate = request.POST.get('plate')
            veh_color = request.POST.get('color')
            veh_owner = request.POST.get('user')
            print(f"{veh_brand} | {veh_model} | {veh_plate} | {veh_plate} | {veh_color}")

            #Verifica preenchimento dos campos
            if len(veh_brand.strip()) == 0 or len(veh_model.strip()) == 0 or len(veh_plate.strip()) == 0 or len(veh_color.strip()) == 0 or len(veh_owner) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('/reg/veh_add')
            else:
                veh_filter_plate = vehicle.objects.filter(plate = veh_plate)

                if veh_filter_plate.exists():
                    messages.add_message(request, constants.ERROR, 'Placa já cadastrada')
                    return redirect('/reg/veh_add')
                else:
                    try:
                        form.save()
                        messages.add_message(request, constants.SUCCESS, 'Veículo cadastrado')
                        return redirect('/reg/veh_add')
                    except:
                        pass
    else:
        form = FormVeh()
                    
    template_name = 'veh_add.html'
    context = {
        'form': form
    }
    
    return render(request, template_name, context)

#2.3 Tela de EDIÇÃO da área Automóvel
def veh_edit(request, vehicle_pk):
    veh_obj = vehicle.objects.get(pk = vehicle_pk)
    form = FormVeh(request.POST or None, instance = veh_obj)
    
    if request.POST:
        if form.is_valid():
            veh_brand = request.POST.get('brand')
            veh_model = request.POST.get('model')
            veh_plate = request.POST.get('plate')
            veh_color = request.POST.get('color')
            veh_owner = request.POST.get('user')

            #Verifica preenchimento dos campos
            if len(veh_brand.strip()) == 0 or len(veh_model.strip()) == 0 or len(veh_plate.strip()) == 0 or len(veh_color.strip()) == 0 or len(veh_owner) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('/reg/veh_add')
            else:
                veh_filter_plate = vehicle.objects.filter(plate = veh_plate)
                if veh_filter_plate.exists():
                    messages.add_message(request, constants.ERROR, 'Placa já cadastrada')
                    return redirect('/reg/veh_add')

                try:
                    form.save()
                    return redirect('/reg/veh')
                except:
                    pass

    template_name = 'veh_edit.html'
    context = {
        'veh_obj': veh_obj,
        'form': form
    }

    return render(request, template_name, context)

#2.4 Função remove da área Automóvel
def veh_remove(vehicle_pk):
    veh_obj = vehicle.objects.get(pk = vehicle_pk)
    veh_obj.delete()

    return redirect('/reg/veh')



