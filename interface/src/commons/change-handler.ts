import { ChangeEvent, useCallback } from 'react';

export type StateUpdater<T> = (value: T | ((prevState: T) => T)) => void;
export type ChangeHandler = (evt: ChangeEvent<HTMLInputElement|HTMLSelectElement>) => void;

export function useChangeHandler<T extends string|undefined>(setCategory: StateUpdater<T>): ChangeHandler {
  return useCallback((evt: ChangeEvent<HTMLInputElement|HTMLSelectElement>) => {
    setCategory(evt.target.value as T);
  }, [setCategory]);
}
