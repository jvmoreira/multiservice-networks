import React, { Fragment, FunctionComponent, ReactElement } from 'react';
import { CategoryField } from '@/components/fields/category-field';
import { FunctionNameField } from '@/components/fields/function-name-field';
import { ClientInterfaceField } from '@/components/fields/client-interface-field';
import { ServerInterfaceField } from '@/components/fields/server-interface-field';
import { NfvTeCategory, NfvTeFunction, useNfvTeValue } from '@/commons/nfv-te-values';
import { TwoRateThreeColorParameters } from './fields/two-rate-three-color-parameters';
import { TokenBucketPolicerParameters } from '@/components/fields/token-bucket-policer-parameters';
import { SingleRateThreeColorParameters } from '@/components/fields/single-rate-three-color-parameters';
import { TokenBucketShaperParameters } from '@/components/fields/token-bucket-shaper-parameters';
import { LeakyBucketParameters } from '@/components/fields/leaky-bucket-parameters';

export function Form(): ReactElement {
  const [category] = useNfvTeValue('category');
  const [functionName] = useNfvTeValue('functionName');
  const NfvTeFunctionParametersComponent = resolveNfvTeFunctionParametersComponent(category, functionName);

  return (
    <form style={{ display: 'flex', flexFlow: 'column', maxWidth: '500px', margin: 'auto' }}>
      <CategoryField />
      <FunctionNameField />

      <NfvTeFunctionParametersComponent />

      <ClientInterfaceField />
      <ServerInterfaceField />
    </form>
  );
}

function resolveNfvTeFunctionParametersComponent(
  category: NfvTeCategory,
  functionName: NfvTeFunction,
): FunctionComponent {
  switch (category) {
    case NfvTeCategory.UNSELECTED:
      return Fragment;
    case NfvTeCategory.SHAPING:
      return resolveNfvTeShapingFunctionsParametersComponent(functionName);
    case NfvTeCategory.POLICING:
      return resolveNfvTePolicingFunctionsParametersComponent(functionName);
    default:
      throw new Error(`Invalid category: ${category}`);
  }
}

function resolveNfvTeShapingFunctionsParametersComponent(functionName: NfvTeFunction): FunctionComponent {
  switch (functionName) {
    case NfvTeFunction.UNSELECTED:
      return Fragment;
    case NfvTeFunction.LEAKY_BUCKET:
      return LeakyBucketParameters;
    case NfvTeFunction.TOKEN_BUCKET:
      return TokenBucketShaperParameters;
    default:
      throw new Error(`Invalid shaping function name: ${functionName}`);
  }
}

function resolveNfvTePolicingFunctionsParametersComponent(functionName: NfvTeFunction): FunctionComponent {
  switch (functionName) {
    case NfvTeFunction.UNSELECTED:
      return Fragment;
    case NfvTeFunction.TOKEN_BUCKET:
      return TokenBucketPolicerParameters;
    case NfvTeFunction.ONE_RATE_THREE_COLOR:
      return SingleRateThreeColorParameters;
    case NfvTeFunction.TWO_RATE_THREE_COLOR:
      return TwoRateThreeColorParameters;
    default:
      throw new Error(`Invalid policing function name: ${functionName}`);
  }
}
