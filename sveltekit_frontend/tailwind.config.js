/** @type {import('tailwindcss').Config} */
export default {
  mode: 'jit',
  darkMode: 'class',
  purge: [
    './public/**/*.html',
    './src/**/*.{js,html,ts,tsx,svelte}',
  ],
  content: [
    './src/**/*.{html,js,svelte,ts}',
    require('path').join(require.resolve(
			'@skeletonlabs/skeleton'),
			'../**/*.{html,js,svelte,ts}'
		)
],
  theme: {
    extend: {},
  },
  plugins: [
    ...require('@skeletonlabs/skeleton/tailwind/skeleton.cjs')()
  ],
}

