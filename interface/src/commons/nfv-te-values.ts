import { createContext, useCallback, useContext, useState } from 'react';
import { StateUpdater } from '@/commons/change-handler';

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

type NfvTeFunctionParameters = Record<string, number>;

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
  const setNfvTeValue = useCallback((newValue: unknown) => {
    setNfvTeValues((currentValues) => ({
      ...currentValues,
      [key]: newValue,
    }));
  }, [key, setNfvTeValues]);

  return [nfvTeValues[key], setNfvTeValue];
}

const defaultNfvTeValues: NfvTeValues = {
  category: NfvTeCategory.UNSELECTED,
  functionName: NfvTeFunction.UNSELECTED,
  functionParameters: {},
  clientInterface: '',
  serverInterface: '',
};
