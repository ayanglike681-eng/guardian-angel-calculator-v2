/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#171717',
        secondary: '#404040',
        cta: '#D4AF37',
        background: '#FFFFFF',
        text: '#171717',
        paper: '#FDFBF7',
        ink: '#334155',
        gold: {
          50: '#FFFBEB',
          100: '#FEF3C7',
          400: '#FBBF24',
          600: '#D97706',
          700: '#B45309',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Times New Roman', 'serif'],
        serif: ['Times New Roman', 'serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      animation: {
        'spin-slow': 'spin 60s linear infinite',
        'stat-reveal': 'statReveal 1.5s ease-out forwards',
        'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
        'pop-in': 'popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) backwards',
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'pulse-slow': 'pulseSlow 3s ease-in-out infinite',
        'spring-pop': 'springPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) backwards',
      },
      keyframes: {
        statReveal: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        popIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        pulseSlow: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
        springPop: {
          '0%': { opacity: '0', transform: 'scale(0.5) translateY(10px)' },
          '70%': { transform: 'scale(1.1) translateY(-2px)' },
          '100%': { opacity: '1', transform: 'scale(1) translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
