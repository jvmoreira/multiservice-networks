import { NfvTeCategory, NfvTeFunction } from '@/commons/nfv-te-values';
import { useMemo } from 'react';

export function useFunctionNameOptions(category: NfvTeCategory): Partial<Record<NfvTeFunction, string>> {
  return useMemo(() => getFunctionNameOptions(category), [category]);
}

export function getFunctionNameOptions(category: NfvTeCategory): Partial<Record<NfvTeFunction, string>> {
  switch (category) {
    case NfvTeCategory.UNSELECTED:
      return {};
    case NfvTeCategory.SHAPING:
      return {
        [NfvTeFunction.LEAKY_BUCKET]: 'Leaky Bucket',
        [NfvTeFunction.TOKEN_BUCKET]: 'Token Bucket',
      };
    case NfvTeCategory.POLICING:
      return {
        [NfvTeFunction.TOKEN_BUCKET]: 'Token Bucket',
        [NfvTeFunction.ONE_RATE_THREE_COLOR]: 'One Rate Three Color',
        [NfvTeFunction.TWO_RATE_THREE_COLOR]: 'Two Rate Three Color',
      };
  }
}
