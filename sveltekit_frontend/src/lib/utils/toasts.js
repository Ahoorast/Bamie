import { toastStore } from '@skeletonlabs/skeleton';

export const success = (message) => {
    const t = {
        message: message,
        background: 'variant-filled-success',
    }
    toastStore.trigger(t);
};

export const failure = (message) => {
    const t = {
        message: message,
        background: 'variant-filled-error',
    }
    toastStore.trigger(t);
};

export const warning = (message) => {
    const t = {
        message: message,
        background: 'variant-filled-warning',
    }
    toastStore.trigger(t);
};