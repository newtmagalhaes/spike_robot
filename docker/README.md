# Exemplo de Aplicação com selenium Grid

1. Execute um dos grids:
    - standalone;
    - hub;
    - selenoid: requer pull manual das imagens listadas em [`browsers.json`](./selenoid/config/browsers.json) (explicação [aqui][selenoid-info])

2. Execute o compose da pasta `app`;

## Exemplo de arquitetura completa do grid

[![grid-archteture]][grid-documentation]

<!-- links -->

[grid-documentation]:https://www.selenium.dev/documentation/grid/components/

[grid-archteture]:https://www.selenium.dev/images/documentation/grid/components.png

[selenoid-info]:https://aerokube.com/selenoid/latest/#_syncing_browser_images_from_existing_file
