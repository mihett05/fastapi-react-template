import i18next from 'i18next';
import { z } from 'zod';
import { zodI18nMap } from 'zod-i18n-map';
// Import your language translation files
import translation from 'zod-i18n-map/locales/ru/zod.json';

// lng and resources key depend on your locale.
i18next.init({
  lng: 'ru',
  resources: {
    ru: { zod: translation },
  },
});
z.setErrorMap(zodI18nMap);

// export configured zod instance
export { z };

export function oneOf<T extends string | number | boolean | bigint | null | undefined>(t: T[]) {
  return z.union([z.literal(t[0]), z.literal(t[1]), ...t.slice(2).map((v) => z.literal(v))]);
}
