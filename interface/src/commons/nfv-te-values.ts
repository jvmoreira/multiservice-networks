import { createContext, useCallback, useContext, useMemo, useState } from 'react';
import { StateUpdater } from './change-handler';

export enum NfvTeCategory {
  UNSELECTED = '',
  POLICING = 'policing',
  SHAPING = 'shaping',
}

export enum NfvTeFunction {
  UNSELECTED = '',
  LEAKY_BUCKET = 'leaky-bucket',
  TOKEN_BUCKET = 'token-bucket',
  ONE_RATE_THREE_COLOR = 'one-rate-three-color',
  TWO_RATE_THREE_COLOR = 'two-rate-three-color',
}

export type NfvTeFunctionParameters = Record<string, string>;

export interface NfvTeValues {
  category: NfvTeCategory,
  functionName: NfvTeFunction,
  functionParameters: NfvTeFunctionParameters,
  clientInterface: string,
  serverInterface: string,
  debug?: 1,
}

interface NfvTeValuesContextType {
  nfvTeValues: NfvTeValues,
  setNfvTeValues: StateUpdater<NfvTeValues>,
}

const nfvTeValuesContext = createContext<NfvTeValuesContextType|null>(null);

export const NfvTeValuesContextProvider = nfvTeValuesContext.Provider;

export function useNfvTeValuesContext(): NfvTeValuesContextType {
  return useContext(nfvTeValuesContext)!;
}

export function useNfvTeValuesState(): [NfvTeValues, StateUpdater<NfvTeValues>] {
  return useState(defaultNfvTeValues);
}

export function useNfvTeValue<Key extends keyof NfvTeValues>(
  key: Key,
): [NfvTeValues[Key], StateUpdater<NfvTeValues[Key]>] {
  const { nfvTeValues, setNfvTeValues } = useNfvTeValuesContext();
  const nfvTeValue = useMemo(() => nfvTeValues[key], [nfvTeValues, key]);

  const setNfvTeValue = useCallback<StateUpdater<NfvTeValues[Key]>>((newValue) => {
    setNfvTeValues((currentValues) => ({
      ...currentValues,
      [key]: (typeof newValue === 'function') ? newValue(currentValues[key]) : newValue,
    }));
  }, [key, setNfvTeValues]);

  return [nfvTeValue, setNfvTeValue];
}

export function useNfvTeFunctionParameters<T extends NfvTeFunctionParameters>(): [T, StateUpdater<T>] {
  return useNfvTeValue('functionParameters') as any as [T, StateUpdater<T>];
}

export function useSetNfvTeFunctionParameter<P extends NfvTeFunctionParameters, Key extends keyof P>(
  key: Key,
  setNfvTeFunctionParameters: StateUpdater<P>,
): StateUpdater<P[Key]> {
  return useCallback<StateUpdater<P[Key]>>((newValue) => {
    setNfvTeFunctionParameters((currentParameters) => ({
      ...currentParameters,
      [key]: (typeof newValue === 'function') ? newValue(currentParameters[key]) : newValue,
    }));
  }, [setNfvTeFunctionParameters, key]);
}

const defaultNfvTeValues: NfvTeValues = {
  category: NfvTeCategory.UNSELECTED,
  functionName: NfvTeFunction.UNSELECTED,
  functionParameters: {},
  clientInterface: '',
  serverInterface: '',
};
