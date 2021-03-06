.. -*- coding: utf-8 -*-

canaimagnulinux.web.locales
===========================

.. contents:: Tabla de Contenidos
   :depth: 2

Introducción
------------

Este producto contiene las `localizaciones`_ de paquetes para 
`sitio web del proyecto Canaima GNU/Linux`_. Esto permite sobreescribir 
las traducciones al Español de Venezuela de ciertos productos Plone.

Características
---------------

- Contiene las localizaciones al Español Venezuela (es-VE) de los siguientes
  paquetes:

  - Producto `canaimagnulinux.userdata`_ para el dominio ``canaimagnulinux.userdata``.

  - Producto `canaimagnulinux.wizard`_ para el dominio ``canaimagnulinux.wizard``.

  - Producto `collective.geo.settings`_ para el dominio ``collective.geo.settings``.

  - Producto `collective.nitf`_ para los dominios ``collective.nitf`` y ``plone``.

  - Producto `pas.plugins.velruse`_ para el dominio ``pas.plugins.velruse``.

  - Producto `plone.app.caching`_ para el dominio ``plone.app.caching``.

  - Producto `plone.app.dexterity`_ para el dominio ``plone.app.dexterity``.

  - Producto `plone.app.discussion`_ para el dominio ``plone.app.discussion``.

  - Producto `plone.app.ldap`_ para el dominio ``plone.app.ldap``.

  - Producto `plone.schemaeditor`_ para el dominio ``plone.schemaeditor``.

  - Producto `Products.PloneServicesCenter`_ para el dominio ``ploneservicescenter``.

  - Producto `quintagroup.analytics`_ para el dominio ``quintagroup.analytics``.

  - Producto `Products.TinyMCE`_ para el dominio ``tinymce``.

  - Producto `z3c.form`_ para el dominio ``z3c.form``.

Uso de scripts
--------------

Para generar y mezclar las traducciones, hay tres (03) dominios, ejecute los siguientes comando:

::

    bin/i18nextract plone
    bin/i18nextract canaimagnulinux.userdata
    bin/i18nextract canaimagnulinux.wizard

Para analizar las platillas ZPT para buscar traducciones perdidas, ejecute el siguiente comando:

::

    bin/i18ncheck canaimagnulinux.wizard


Usted puede enviar el nombre de la plantilla como un parámetro, sin la ruta, ejecute el siguiente comando:

::

    bin/i18ncheck canaimagnulinux.wizard intro.pt

Creación
--------

Este producto fue creado por la comunidad Canaima y Plone Venezuela, en varias sesiones a distancia entre fines de semanas horas nocturnas de trabajo y Capapas Canaima:

http://canaima.softwarelibre.gob.ve/

https://plone.org/countries/ve

¡Especial agradecimiento a Flamel Canto, Jin Kadaba y Leonardo J. Caballero G.!

Instalación
-----------

Usted puede leer el archivo ``INSTALL.txt`` dentro del directorio ``docs`` de
este paquete.

Descargas
---------

Usted puede encontrar la versión de desarrollo del paquete ``canaimagnulinux.web.locales``
en el `repositorio CanaimaGNULinux`_ en GitHub.com.

¿Tienes una idea?, ¿Encontraste un error? Háganos saber mediante la `apertura de un ticket de soporte`_.

Contribuye
----------

- Seguimiento de incidencia: http://github.com/CanaimaGNULinux/canaimagnulinux.web.locales/issues

- Cogido fuente: http://github.com/CanaimaGNULinux/canaimagnulinux.web.locales

- Sitio web: http://canaima.softwarelibre.gob.ve/

Soporte
-------

Si usted tiene alguna incidencia, por favor, hágalo saber a nosotros, enviando un ticket con el reporte http://github.com/CanaimaGNULinux/canaimagnulinux.web.locales/issues

Licencia
--------

Este proyecto esta licenciado bajo la GNU General Public License v2 (GPLv2).

----

Calidad del proyecto
--------------------

Sobre todo este producto es inofensivo!!!

.. image:: https://secure.travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.locales.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/CanaimaGNULinux/canaimagnulinux.web.locales

.. image:: https://coveralls.io/repos/CanaimaGNULinux/canaimagnulinux.web.locales/badge.svg?branch=master&service=github
    :alt: Coveralls badge
    :target: https://coveralls.io/github/CanaimaGNULinux/canaimagnulinux.web.locales?branch=master

.. image:: https://d2weczhvl823v0.cloudfront.net/CanaimaGNULinux/canaimagnulinux.web.locales/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free


Autor(es) Original(es)
----------------------

* Leonardo J .Caballero G. aka macagua

Colaboraciones impresionantes
-----------------------------

* Flamel Canto aka flamelcanto

* Jin Kadaba aka Unknown


Para una lista actualizada de todo los colaboradores visite:
https://github.com/canaimagnulinux/canaimagnulinux.web.locales/contributors

.. _`sitio web del proyecto Canaima GNU/Linux`: http://canaima.softwarelibre.gob.ve/
.. _`localizaciones`: http://es.wikipedia.org/wiki/Internacionalización_y_localización
.. _`canaimagnulinux.userdata`: https://github.com/CanaimaGNULinux/canaimagnulinux.userdata
.. _`canaimagnulinux.wizard`: https://github.com/CanaimaGNULinux/canaimagnulinux.wizard
.. _`collective.geo.settings`: https://pypi.python.org/pypi/collective.geo.settings
.. _`collective.nitf`: https://github.com/collective/collective.nitf
.. _`pas.plugins.velruse`: https://pypi.python.org/pypi/pas.plugins.velruse
.. _`plone.app.caching`: https://pypi.python.org/pypi/plone.app.caching
.. _`plone.app.dexterity`: https://pypi.python.org/pypi/plone.app.dexterity
.. _`plone.app.discussion`: https://pypi.python.org/pypi/plone.app.discussion
.. _`plone.app.ldap`: https://pypi.python.org/pypi/plone.app.ldap
.. _`plone.schemaeditor`: https://pypi.python.org/pypi/plone.schemaeditor
.. _`Products.PloneServicesCenter`: https://pypi.python.org/pypi/Products.PloneServicesCenter
.. _`quintagroup.analytics`: https://pypi.python.org/pypi/quintagroup.analytics
.. _`Products.TinyMCE`: https://pypi.python.org/pypi/Products.TinyMCE
.. _`z3c.form`: https://pypi.python.org/pypi/z3c.form
.. _`repositorio CanaimaGNULinux`: https://github.com/CanaimaGNULinux/canaimagnulinux.web.locales
.. _apertura de un ticket de soporte: https://github.com/CanaimaGNULinux/canaimagnulinux.web.locales/issues
