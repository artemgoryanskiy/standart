from django.shortcuts import render


def lab_prot_view(request, slug):
    if slug == 'specialnaya-ocenka-uslovij-truda-sout':
        return render(request, 'services_templates/lab_prot/lab_prot_spec.html', context={})
    elif slug == 'ocenka-professionalnyh-riskov':
        return render(request, 'services_templates/lab_prot/lab_prot_risks.html', context={})
    elif slug == 'razrabotka-komplekta-dokumentov-po-ohrane-truda':
        return render(request, 'services_templates/lab_prot/lab_prot_doc.html', context={})
    elif slug == 'autsorsing-po-ohrane-truda':
        return render(request, 'services_templates/lab_prot/lab_prot_outsourcing.html', context={})
