from django.shortcuts import render


def ecology_view(request, slug):
    if slug == 'pasporta-othodov':
        return render(request, 'services_templates/ecology/ecology_eco_pass.html', context={})
    elif slug == 'inventarizaciya-istochnikov-i-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh':
        return render(request, 'services_templates/ecology/ecology_inventory.html', context={})
    elif slug == 'postanovka-na-uchet-obektov-negativnogo-vozdejstviya-na-okruzhayushuyu-sredu-nvos':
        return render(request, 'services_templates/ecology/ecology_registration.html', context={})
    elif slug == 'meropriyatiya-po-umensheniyu-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh-v-periody-neblagopriyatnyh-meteorologicheskih-uslovij-nmu':
        return render(request, 'services_templates/ecology/ecology_nmu.html', context={})
    elif slug == 'proekt-predelno-dopustimyh-vybrosov-v-atmosferu-proekt-pdv':
        return render(request, 'services_templates/ecology/ecology_project.html', context={})
    elif slug == 'ekologicheskaya-otchetnost':
        return render(request, 'services_templates/ecology/ecology_report.html', context={})
