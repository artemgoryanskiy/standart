from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from app_prof_dev.models import CategoryProfDev
from app_prof_retraining.models import CategoryProfRetrain
from app_prof_training.models import CategoryProfTrain


class CategoryProfDevSitemap(Sitemap):
    # define how often your website will change, the priority, and the protocol used to access your site
    changefreq = 'weekly'  # can be weekly daily always monthly yearly or never
    priority = 1.0  # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    # define the posts you want in your sitemap here
    def items(self):
        return CategoryProfDev.objects.all()

    def location(self, obj):
        return f'/education-prof-dev/{obj.slug}'


class CategoryProfRetrainSitemap(Sitemap):
    # define how often your website will change, the priority, and the protocol used to access your site
    changefreq = 'weekly'  # can be weekly daily always monthly yearly or never
    priority = 1.0  # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    # define the posts you want in your sitemap here
    def items(self):
        return CategoryProfRetrain.objects.all()

    def location(self, obj):
        return f'/education-prof-retr/{obj.slug}'


class CategoryProfTrainSitemap(Sitemap):
    # define how often your website will change, the priority, and the protocol used to access your site
    changefreq = 'weekly'  # can be weekly daily always monthly yearly or never
    priority = 1.0  # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    # define the posts you want in your sitemap here
    def items(self):
        return CategoryProfTrain.objects.all()

    def location(self, obj):
        return f'/education-prof-train/{obj.slug}'


class EcoPassSitemap(Sitemap):
    def items(self):
        return ['pasporta-othodov']

    def location(self, slug='pasporta-othodov'):
        return f'/services/ecology/{slug}'


class EcoInvSitemap(Sitemap):
    def items(self):
        return ['inventarizaciya-istochnikov-i-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh']

    def location(self, slug='inventarizaciya-istochnikov-i-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh'):
        return f'/services/ecology/{slug}'


class EcoNmuSitemap(Sitemap):
    def items(self):
        return ['meropriyatiya-po-umensheniyu-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh-v-periody-neblagopriyatnyh-meteorologicheskih-uslovij-nmu']

    def location(self, slug='meropriyatiya-po-umensheniyu-vybrosov-zagryaznyayushih-veshestv-v-atmosfernyj-vozduh-v-periody-neblagopriyatnyh-meteorologicheskih-uslovij-nmu'):
        return f'/services/ecology/{slug}'


class EcoPdvSitemap(Sitemap):
    def items(self):
        return ['proekt-predelno-dopustimyh-vybrosov-v-atmosferu-proekt-pdv']

    def location(self, slug='proekt-predelno-dopustimyh-vybrosov-v-atmosferu-proekt-pdv'):
        return f'/services/ecology/{slug}'


class EcoRegSitemap(Sitemap):
    def items(self):
        return ['postanovka-na-uchet-obektov-negativnogo-vozdejstviya-na-okruzhayushuyu-sredu-nvos']

    def location(self, slug='postanovka-na-uchet-obektov-negativnogo-vozdejstviya-na-okruzhayushuyu-sredu-nvos'):
        return f'/services/ecology/{slug}'


class EcoRepSitemap(Sitemap):
    def items(self):
        return ['ekologicheskaya-otchetnost']

    def location(self, slug='ekologicheskaya-otchetnost'):
        return f'/services/ecology/{slug}'


class LabDocSitemap(Sitemap):
    def items(self):
        return ['razrabotka-komplekta-dokumentov-po-ohrane-truda']

    def location(self, slug='razrabotka-komplekta-dokumentov-po-ohrane-truda'):
        return f'/services/lab-prot/{slug}'


class LabOutSitemap(Sitemap):
    def items(self):
        return ['autsorsing-po-ohrane-truda']

    def location(self, slug='autsorsing-po-ohrane-truda'):
        return f'/services/lab-prot/{slug}'


class LabRiskSitemap(Sitemap):
    def items(self):
        return ['ocenka-professionalnyh-riskov']

    def location(self, slug='ocenka-professionalnyh-riskov'):
        return f'/services/lab-prot/{slug}'


class LabSoutSitemap(Sitemap):
    def items(self):
        return ['specialnaya-ocenka-uslovij-truda-sout']

    def location(self, slug='specialnaya-ocenka-uslovij-truda-sout'):
        return f'/services/lab-prot/{slug}'


class ContactSitemap(Sitemap):
    def items(self):
        return ['/about-us/contacts']

    def location(self, text='/about-us/contacts'):
        return f'{text}'


class MainPageSitemap(Sitemap):
    def items(self):
        return ['main']

    def location(self, item):
        return reverse(item)
